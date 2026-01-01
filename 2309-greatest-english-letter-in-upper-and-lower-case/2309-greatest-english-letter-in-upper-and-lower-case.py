class Solution:
    def greatestLetter(self, s: str) -> str:
        res=""
        for ch in s:
            if ch.lower() in s and ch.upper() in s:
                res=max(res,ch.upper())
        return res