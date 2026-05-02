class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        freq = Counter(sentence)
        return len(freq) == 26