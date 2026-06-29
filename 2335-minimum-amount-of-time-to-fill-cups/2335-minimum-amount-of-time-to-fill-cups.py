class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount.sort()
        
        a = amount[0]
        b = amount[1]
        c = amount[2]

        if c > a+b:
            return c
        else:
            total = a+b+c

            if total % 2 == 0:
                return total // 2
            else:
                return total // 2 + 1