class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res=0
        for i in s:
            res ^= ord(i)
        for ch in t:
            res ^= ord(ch)
        return chr(res)
