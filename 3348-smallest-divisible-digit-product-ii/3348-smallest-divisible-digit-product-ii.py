class Solution(object):
    def smallestNumber(self, num, t):
        """
        :type num: str
        :type t: int
        :rtype: str
        """
        # Step 1: Validate prime factors of t
        temp = t
        for p in [2, 3, 5, 7]:
            while temp % p == 0:
                temp //= p
        if temp > 1:
            return "-1"

        digit_counts = {
            1: (0, 0, 0, 0),
            2: (1, 0, 0, 0),
            3: (0, 1, 0, 0),
            4: (2, 0, 0, 0),
            5: (0, 0, 1, 0),
            6: (1, 1, 0, 0),
            7: (0, 0, 0, 1),
            8: (3, 0, 0, 0),
            9: (0, 2, 0, 0)
        }
        
        # Calculate target prime factor requirements for t (2, 3, 5, 7)
        t_factors = [0, 0, 0, 0]
        temp = t
        for idx, p in enumerate([2, 3, 5, 7]):
            while temp % p == 0:
                t_factors[idx] += 1
                temp //= p
                
        # Minimum digits required to cover remaining factor counts
        def get_min_digits(r2, r3, r5, r7):
            r2, r3, r5, r7 = max(0, r2), max(0, r3), max(0, r5), max(0, r7)
            min_len = float('inf')
            
            for c6 in range(3):
                rem_3 = max(0, r3 - c6)
                rem_2 = max(0, r2 - c6)
                
                c9, c3 = rem_3 // 2, rem_3 % 2
                c8 = rem_2 // 3
                rem_2_left = rem_2 % 3
                c4, c2 = rem_2_left // 2, rem_2_left % 2
                
                min_len = min(min_len, r5 + r7 + c6 + c9 + c3 + c8 + c4 + c2)
            return min_len

        # Construct the lexicographically smallest valid suffix of length rem_len
        def make_suffix(rem_len, r2, r3, r5, r7):
            r2, r3, r5, r7 = max(0, r2), max(0, r3), max(0, r5), max(0, r7)
            best_suffix_str = None
            
            for c6 in range(3):
                rem_3 = max(0, r3 - c6)
                rem_2 = max(0, r2 - c6)
                
                c9, c3 = rem_3 // 2, rem_3 % 2
                c8 = rem_2 // 3
                rem_2_left = rem_2 % 3
                c4, c2 = rem_2_left // 2, rem_2_left % 2
                
                total = r5 + r7 + c6 + c9 + c3 + c8 + c4 + c2
                if total <= rem_len:
                    digits = []
                    digits.extend(['2'] * c2)
                    digits.extend(['3'] * c3)
                    digits.extend(['4'] * c4)
                    digits.extend(['5'] * r5)
                    digits.extend(['6'] * c6)
                    digits.extend(['7'] * r7)
                    digits.extend(['8'] * c8)
                    digits.extend(['9'] * c9)
                    digits.sort()
                    
                    full_suffix = ['1'] * (rem_len - len(digits)) + digits
                    suffix_str = "".join(full_suffix)
                    
                    if best_suffix_str is None or suffix_str < best_suffix_str:
                        best_suffix_str = suffix_str
                                
            return list(best_suffix_str) if best_suffix_str is not None else None

        n = len(num)
        
        # Check if num itself is already valid
        if '0' not in num:
            curr_factors = [0, 0, 0, 0]
            for ch in num:
                d = int(ch)
                for idx, p in enumerate([2, 3, 5, 7]):
                    curr_factors[idx] += digit_counts[d][idx]
            if all(curr_factors[i] >= t_factors[i] for i in range(4)):
                return num

        first_zero = num.find('0')
        limit = first_zero if first_zero != -1 else n - 1
        
        pref = [[0, 0, 0, 0]]
        for ch in num:
            d = int(ch)
            cur = pref[-1][:]
            if d > 0:
                for idx, p in enumerate([2, 3, 5, 7]):
                    cur[idx] += digit_counts[d][idx]
            pref.append(cur)
            
        # Try right-to-left matching for same length n
        for i in range(limit, -1, -1):
            curr_d = int(num[i])
            for d in range(curr_d + 1, 10):
                r2 = t_factors[0] - pref[i][0] - digit_counts[d][0]
                r3 = t_factors[1] - pref[i][1] - digit_counts[d][1]
                r5 = t_factors[2] - pref[i][2] - digit_counts[d][2]
                r7 = t_factors[3] - pref[i][3] - digit_counts[d][3]
                
                rem_len = n - 1 - i
                if get_min_digits(r2, r3, r5, r7) <= rem_len:
                    suf = make_suffix(rem_len, r2, r3, r5, r7)
                    if suf is not None:
                        return num[:i] + str(d) + "".join(suf)
                        
        # Otherwise, expand to the minimum necessary length
        min_len_needed = max(n + 1, get_min_digits(t_factors[0], t_factors[1], t_factors[2], t_factors[3]))
        suf = make_suffix(min_len_needed, t_factors[0], t_factors[1], t_factors[2], t_factors[3])
        return "".join(suf)