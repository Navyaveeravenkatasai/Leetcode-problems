class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        count=0
        for ch in word:
            if ord('A') <= ord(ch) <= ord('Z'):
                count+=1
        
        if count == len(word):
            return True
        
        if count == 0:
            return True
        
        if count == 1 and ord('A') <= ord(word[0]) <= ord('Z'):
            return True
        return False