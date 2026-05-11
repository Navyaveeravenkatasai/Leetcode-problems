class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s=list(s)
        left=0
        right=len(s)-1
        for i in range(len(s)):
            if s[left] > s[right]:
                s[left] = s[right]
            elif s[right] > s[left]:
                s[right] = s[left]
            left+=1
            right-=1
        return ''.join(s)