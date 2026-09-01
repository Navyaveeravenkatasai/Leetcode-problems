class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        freq={}

        n = len(nums)

        freq[nums[0]] = 1

        for i in range(1,n):
            if nums[i] != nums[i-1]:
                freq[nums[i]] = freq.get(nums[i],0) + 1

        count = 0

        for value in freq.values():
            if value == 1:
                count += 1

        return count