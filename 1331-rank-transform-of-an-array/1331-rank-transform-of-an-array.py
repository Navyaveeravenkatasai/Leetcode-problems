class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        res1 = sorted(set(arr))    

        freq = {}
        i = 1

        for ch in res1:
            freq[ch] = i            
            i += 1

        res = []

        for ch in arr:
            res.append(freq[ch])    

        return res