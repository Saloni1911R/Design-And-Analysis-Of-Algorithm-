class Solution(object):
    def totalNumbers(self, digits):
        """:type digits: List[int] :rtype: int"""
        from collections import Counter
        
        # Count the frequency of each digit in the input array
        digit_count = Counter(digits)
        unique_even_count = 0
        
        # Check all 3-digit even numbers
        for num in range(100, 1000, 2):
            num_count = Counter(int(d) for d in str(num))
            
            # Verify if we have enough of each digit to form the number
            if all(digit_count[d] >= num_count[d] for d in num_count):
                unique_even_count += 1
                
        return unique_even_count
