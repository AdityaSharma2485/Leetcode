class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            string = ''
            j = 0
            for i in word:
                if i == ch:
                    return word[j] + string + word[j+1:]
                else:
                    string = i + string
                    j += 1
        else:
            return word
