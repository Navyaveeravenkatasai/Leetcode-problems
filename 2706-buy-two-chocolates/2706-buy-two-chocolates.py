class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()

        for ch in range(0,len(prices)):
            total = prices[0] + prices[1]
        
        if total == money:
            return 0
        elif total <= money:
            return money - total
        else:
            return money