class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        if len(cost) <=2:
            return sum(cost)
        cost.sort(reverse=True)
        res=[]
        
        for i in range(len(cost)):
            if (i+1) % 3 == 0:
                continue
            else:
                res.append(cost[i])
        return sum(res)