class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        n = str(n)
        n = list(n)
        mini = float('inf')
        freq = {}

        for ch in n:
            freq[ch] = freq.get(ch, 0) + 1

        min_freq = float('inf')

        for key in freq:
            if freq[key] < min_freq:
                min_freq = freq[key]
                mini = int(key)
            elif freq[key] == min_freq:
                mini = min(mini, int(key))

        return mini