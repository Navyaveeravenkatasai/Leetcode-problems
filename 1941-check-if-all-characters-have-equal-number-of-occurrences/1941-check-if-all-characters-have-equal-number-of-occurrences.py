class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        s=list(s)
        freq={}
        for ch in s:
            freq[ch] = freq.get(ch,0) + 1
        res=set()
        for key in freq.values():
            if key not in res:
                res.add(key)
        if  len(res) == 1:
            return True
        return False