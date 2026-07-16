class Solution:
    def convertDateToBinary(self, date: str) -> str:
        tot = date.split('-')
        n = len(tot)
        res = ""
        for ch in tot:
            res += bin(int(ch))[2:]
            res += '-'
        total = res[:-1]

        return total