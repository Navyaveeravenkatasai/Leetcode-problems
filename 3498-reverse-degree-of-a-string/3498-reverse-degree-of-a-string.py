class Solution:
    def reverseDegree(self, s: str) -> int:
        res=0
        value=0
        for ch in range(len(s)):
            value = ord('z') - ord(s[ch])  + 1
            res += value *(ch + 1)
        return res