class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        total = 0
        maxi=max(nums)
        for i in range(k):
            total += maxi
            nums.append(total)
            maxi += 1
        return nums[-1]