class Solution:
    def minimumFlips(self, n: int) -> int:
        res = bin(n)[2:]
        res = list(res)
        tot = list(res)[::-1]
        count = 0
        for ch in range(len(res)):
            if res[ch] == tot[ch]:
                continue
            else:
                count += 1

        return count