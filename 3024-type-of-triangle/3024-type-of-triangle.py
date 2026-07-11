class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        a = nums[0]
        b = nums[1]
        c = nums[2]

        if a + b <= c:
            return "none"

        if a == b == c:
            return "equilateral"
        elif a < b < c:
            return "scalene"
        else:
            return "isosceles"