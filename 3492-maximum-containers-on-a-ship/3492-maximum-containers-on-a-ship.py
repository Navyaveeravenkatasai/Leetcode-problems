class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        res = 0
        if w == maxWeight:
            return 1
        for i in range(n*n):  
            if (n* n) * w <= maxWeight:
                return n*n
        
        for i in range(n*n):
            if (n* n) * w > maxWeight:
                for i in range(1,n*n):
                    if i * w <= maxWeight:
                        res=max(res,i)
            return res