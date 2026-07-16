class Solution:
    def convertDateToBinary(self, date: str) -> str:
        tot = date.split('-')
        res = ""

        for ch in tot:
            res += bin(int(ch))[2:]
            res += '-'

        return res[:-1]