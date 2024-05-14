class Solution:
    def isVowel(self, char: str) -> bool:
        vowels = set('aeiouAEIOU')
        return char in vowels

    def halvesAreAlike(self, s: str) -> bool:
        mid = len(s) // 2
        count_a = sum(1 for char in s[:mid] if self.isVowel(char))
        count_b = sum(1 for char in s[mid:] if self.isVowel(char))
        return count_a == count_b
