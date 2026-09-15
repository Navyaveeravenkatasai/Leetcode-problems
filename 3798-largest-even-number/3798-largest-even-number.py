class Solution:
    def largestEven(self, s: str) -> str:
        while len(s) > 0:
            if s[-1] in "02468":
                return s
            else:
                s = s[:-1]

        return ""