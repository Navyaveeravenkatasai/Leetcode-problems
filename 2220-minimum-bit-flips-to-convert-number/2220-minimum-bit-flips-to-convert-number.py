class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        s1 = bin(start)[2:]
        g1 = bin(goal)[2:]
        max_len = max(len(s1), len(g1))

        s1 = s1.zfill(max_len)
        g1 = g1.zfill(max_len)
        
        count = 0
        n = len(s1)-1
        for i in range(n,-1,-1):
            if s1[i] == g1[i]:
                continue
            else:
                count += 1

        return count 