class Solution:
    def mirrorDistance(self, n: int) -> int:
        res=0
        m = int(str(n)[::-1])
        return abs(n - m)