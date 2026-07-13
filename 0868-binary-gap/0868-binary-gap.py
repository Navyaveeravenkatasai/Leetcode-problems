class Solution:
    def binaryGap(self, n: int) -> int:
        n = bin(n)[2:]
        res = []
        i = 0
        for ch in n:
            if ch == '1':
                res.append(i)
                i += 1
            else:
                i += 1
        if len(res) == 1:
            return 0
        res1 = 0
        for ch in range(1,len(res)):
            tot = res[ch] - res[ch-1]
            res1 = max(res1,tot)

        return res1


