class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # Function to count character occurrences in a string
        def count_characters(string):
            char_count = {}
            for char in string:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
            return char_count
        
        # Count character occurrences in both strings
        s_count = count_characters(s)
        t_count = count_characters(t)
        
        # Compare the counts of characters in both hashmaps
        return s_count == t_count
