class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        res=[]
        lst=s.split(" ")
        for i in range(k):
            res.append(lst[i])
        total=" ".join(res)
        return total

