class Solution:
    def countDigits(self, num: int) -> int:
        if num < 10:
            return 1
        count = 0
        tot = list(str(num))
        for ch in tot:
            if num % int(ch) == 0:
                count +=1

        return count