class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq={}

        for ch in words:
            freq[ch] = freq.get(ch,0) + 1
        res=[]
        count =0
        for word,frequency in sorted(freq.items(),key =lambda x:(-x[1], x[0])):
            if count < k:
                res.append(word)
                count += 1
        return res
            