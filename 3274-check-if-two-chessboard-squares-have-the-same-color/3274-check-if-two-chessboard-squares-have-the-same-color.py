class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        a = ord(coordinate1[0]) + int(coordinate1[1])
        b = ord(coordinate2[0]) + int(coordinate2[1])

        return a % 2 == b % 2
