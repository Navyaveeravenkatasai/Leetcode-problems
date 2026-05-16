class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        values = list(freq.values())
        if len(values) <= k:
            return 0
        values.sort()
        delete = 0
        remove = len(values) - k
        for i in range(remove):
            delete += values[i]
        return delete