class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper():
            return True
        return False