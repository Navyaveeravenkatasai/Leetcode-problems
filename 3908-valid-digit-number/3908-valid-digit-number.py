class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        n = list(str(n))
        if str(x) in n and int(n[0]) != x:
            return True
        return False