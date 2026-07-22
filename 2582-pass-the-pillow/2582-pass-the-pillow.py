class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        ans = 0
        step = n-1
        complete = time // step
        remaining = time % step

        if complete % 2 == 0:
            ans = 1 + remaining
        else:
            ans = n - remaining
        return ans 

        