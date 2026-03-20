class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        word=list(word)
        left=0
        right=word.index(ch) if ch in word else -1
        while left < right:
                word[right],word[left] = word[left],word[right]
                left+=1
                right-=1
        return "".join(word)