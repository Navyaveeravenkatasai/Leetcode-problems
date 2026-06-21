class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        res = 0
        count = 0
        
        if coins < costs[0]:
            return 0
        for i in range(len(costs)):
            res += costs[i]
            if res <= coins:
                count += 1
            

        return count