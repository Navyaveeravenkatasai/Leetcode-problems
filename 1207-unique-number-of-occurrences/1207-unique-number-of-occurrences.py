class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq={}

        for ch in arr:
            freq[ch] = freq.get(ch,0) + 1
        
        res=set()
        for key in freq.values():
            if key in res:
                return False
            res.add(key)
        return True