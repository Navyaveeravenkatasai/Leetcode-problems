class Solution:
    def addDigits(self, num: int) -> int:
        res = 0

        digit = num % 10
        num = num // 10
        res = digit + num
        while  res > 9:
            digit = res % 10
            num = res // 10
            res = digit + num
        return res