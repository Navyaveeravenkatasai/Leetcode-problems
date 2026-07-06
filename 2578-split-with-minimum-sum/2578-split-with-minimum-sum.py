class Solution:
    def splitNum(self, num: int) -> int:
        num = list(str(num))
        num.sort()
        res = []
        tot = []
        for ch in range(0,len(num),2):
            res.append(num[ch])
        res = int("".join(map(str, res)))
        for ch in range(1,len(num),2):
            tot.append(num[ch])
        tot = int("".join(map(str, tot)))
        return tot + res