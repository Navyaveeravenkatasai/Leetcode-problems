class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        res=[]
        n = 100000
        for i in range(n):
            res.append(i*i)

        if num in res:
            return True
        return False