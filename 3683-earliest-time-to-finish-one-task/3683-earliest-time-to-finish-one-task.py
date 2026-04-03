class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        tot=float('inf')
        for num in tasks:
            res=0
            for i in range(len(num)):
                res += num[i]
            tot = min(res,tot)
        return tot