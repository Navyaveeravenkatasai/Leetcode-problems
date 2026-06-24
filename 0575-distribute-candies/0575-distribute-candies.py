class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)
        seti = list(set(candyType))
        count = 0
        for ch in seti:
            count +=1
            if count > n // 2:
                count = count - 1
        return count