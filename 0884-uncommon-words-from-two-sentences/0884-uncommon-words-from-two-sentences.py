class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1=list(s1.split(' '))
        s2=list(s2.split(' '))
        s= s1 + s2
        freq={}
        for ch in s:
            freq[ch] = freq.get(ch,0) + 1
        res=[]
        for key,value in freq.items():
            if value == 1:
                res.append(key)
        return res