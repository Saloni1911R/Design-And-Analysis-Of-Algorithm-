class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :type : int
        """
        total_degree = 0
        
        for i, char in enumerate(s):
            # Calculate 1-indexed position in the string
            string_index = i + 1
            
            # 'a' -> 26, 'b' -> 25, ..., 'z' -> 1
            # ord('z') - ord(char) + 1 yields this exact mapping
            reversed_alphabet_index = ord('z') - ord(char) + 1
            
            # Accumulate the product
            total_degree += reversed_alphabet_index * string_index
            
        return total_degree
