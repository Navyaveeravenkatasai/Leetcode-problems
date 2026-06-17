class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        tot= list(str(x))
        res=0
        for ch in tot:
            res+=int(ch)

        if x % res == 0:
            return res
        else:
            return -1