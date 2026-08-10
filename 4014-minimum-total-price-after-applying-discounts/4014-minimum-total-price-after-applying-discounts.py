class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort()
        discounts.sort()
        a = len(prices)-1
        b = len(discounts)-1
        sumi = 0.0


        while a >= 0 and b >= 0:
            sumi += (prices[a] * (100 - discounts[b])) / 100
            a -= 1
            b -= 1
        
        while a >= 0:
            sumi += prices[a]
            a -= 1
            
        return sumi
