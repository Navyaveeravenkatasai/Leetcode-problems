class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq = {}
        for ch in word:
            freq[ch] = freq.get(ch, 0) + 1
        for ch in freq:
            freq[ch] -= 1
            counts = []
            for key in freq:
                if freq[key] > 0:
                    counts.append(freq[key])
            if len(set(counts)) == 1:
                return True
            freq[ch] += 1
        return False