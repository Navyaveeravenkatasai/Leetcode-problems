class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []

        for ch in range(len(words)):
                if x in words[ch]:
                    res .append(ch)

        return res