class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        freq={}
        for ch in words:
            for i in ch:
                freq[i] = freq.get(i,0) + 1
        
        for value in freq.values():
            if value % n != 0:
                return False
        return True