class Solution:
    def smallestNumber(self, n: int) -> int:
        a = bin(n)[2:]
        n = len(a)
        count = 1
        res = "1" * n
        final = int(res,2)

        return final
                