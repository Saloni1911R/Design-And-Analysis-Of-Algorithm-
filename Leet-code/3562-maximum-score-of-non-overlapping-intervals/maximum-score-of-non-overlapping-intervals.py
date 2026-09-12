import bisect

class Solution(object):
    def maximumWeight(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        # Step 1: Pack intervals with their original index and sort by start time
        # Each element becomes: (start, end, weight, original_index)
        sorted_intervals = sorted(
            (interval[0], interval[1], interval[2], i) 
            for i, interval in enumerate(intervals)
        )
        
        n = len(sorted_intervals)
        
        # Step 2: Initialize DP table
        # dp[i][quota] stores a tuple: (max_weight, tuple_of_selected_indices)
        # quota ranges from 0 to 4
        dp = [[(0, ())] * 5 for _ in range(n + 1)]
        
        # Step 3: Fill the DP table bottom-up
        for i in range(n - 1, -1, -1):
            l, r, weight, original_idx = sorted_intervals[i]
            
            # Find the next non-overlapping interval index where next_l > r
            # Using float('inf') ensures we jump past any intervals starting at <= r
            next_idx = bisect.bisect_right(sorted_intervals, (r, float('inf')))
            
            for quota in range(1, 5):
                # Choice 1: Skip the current interval
                skip_weight, skip_indices = dp[i + 1][quota]
                
                # Choice 2: Pick the current interval
                next_weight, next_indices = dp[next_idx][quota - 1]
                pick_weight = weight + next_weight
                # Keep the selected indices sorted to comply with lexicographical comparison
                pick_indices = tuple(sorted((original_idx,) + next_indices))
                
                # Decision making with tie-breaking
                if pick_weight > skip_weight:
                    dp[i][quota] = (pick_weight, pick_indices)
                elif skip_weight > pick_weight:
                    dp[i][quota] = (skip_weight, skip_indices)
                else:
                    # If weights are equal, choose the lexicographically smaller indices
                    if pick_indices < skip_indices:
                        dp[i][quota] = (pick_weight, pick_indices)
                    else:
                        dp[i][quota] = (skip_weight, skip_indices)
                        
        # The answer is the best collection of indices starting from index 0 with up to 4 intervals
        return list(dp[0][4][1])
