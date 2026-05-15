class Solution:
    def maxProduct(self, n: int) -> int:
        n = list(str(n))
        n.sort(reverse = True)
        n=n[:2]
        res = []
        total = 1
        for ch in n:
            total *= int(ch)
        res.append(str(total))
        res = int(''.join(res))

        return res