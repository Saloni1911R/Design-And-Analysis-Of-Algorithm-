class Solution(object):
    def findKthSmallest(self, coins, k):
        """
        :type coins: List[int]
        :type k: int
        :rtype: int
        """
        # Custom GCD implementation for Python 2 compatibility
        def get_gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        n = len(coins)
        subsets = []
        
        # Precompute the LCM and sign for all possible subsets of coins
        for i in range(1, 1 << n):
            current_lcm = 1
            bits_count = 0
            for j in range(n):
                if (i >> j) & 1:
                    bits_count += 1
                    gcd = get_gcd(current_lcm, coins[j])
                    current_lcm = (current_lcm * coins[j]) // gcd
            
            # Odd number of elements -> +1, Even number of elements -> -1
            sign = 1 if bits_count % 2 == 1 else -1
            subsets.append((current_lcm, sign))
            
        # Helper function to count how many distinct multiples exist <= target
        def count_multiples_under(target):
            total = 0
            for lcm, sign in subsets:
                total += sign * (target // lcm)
            return total

        # Binary search space range
        low = min(coins)
        high = min(coins) * k
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if count_multiples_under(mid) >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans
