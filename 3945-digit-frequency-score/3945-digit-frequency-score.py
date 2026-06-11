class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        freq={}
        res = 0
        n=list(str(n))

        for ch in n:
            freq[ch] = freq.get(ch,0) + 1

        for key,value in freq.items():
            res += (int(key) * value)
        return res

        
