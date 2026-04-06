class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        res=[]
        for ch in words:
            res.append(ch[0])
        total=0
        total = "".join(res)

        if total == s:
            return True
        else:
            return False