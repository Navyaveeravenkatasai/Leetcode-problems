class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total=0

        for num in nums:
            div=set()

            for i in range(1, int(math.sqrt(num)) + 1):
                if num % i ==0:
                    div.add(i)
                    div.add(num // i)

            if len(div) == 4:
                total+=sum(div)

        return total