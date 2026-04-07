class Solution:
    def maxDistinct(self, s: str) -> int:
        s=set(s)
        freq = {}
        total = 0
        for ch in s:
            freq[ch] = freq.get(ch,0) + 1

        for key in freq.values():
            total += key
        return total