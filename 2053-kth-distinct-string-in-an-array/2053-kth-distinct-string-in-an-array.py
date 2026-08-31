class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq={}
        res = []
        for ch in arr:
            freq[ch] = freq.get(ch,0) + 1

        for key,value in freq.items():
            if value == 1:
                res.append(key)

        if k > len(res):
            return ""
        return res[k-1]
        
        
        