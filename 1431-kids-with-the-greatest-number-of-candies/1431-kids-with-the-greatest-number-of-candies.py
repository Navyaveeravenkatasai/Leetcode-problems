class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi=max(candies)
        res=[]
        for num in range(len(candies)):
            if candies[num] + extraCandies >= maxi:
                res.append(True)
            else:
                res.append(False)
        return res