class Solution:
    def findComplement(self, num: int) -> int:
        num = bin(num)[2:]
        res = ""

        for ch in num:
            if ch == '0':
                res += "1"
            else:
                res += "0"
        
        decimal = 0
        power = 0
        n = len(res) - 1

        while n >= 0:
            decimal += int(res[n]) * (2 ** power)
            power += 1
            n -= 1

        return decimal 