class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        if len(nums) == 1:
            return [0]
        res = []
        for ch in range(0,len(nums)):
            if nums[ch] % 2 != 0:
                count = 0
                for i in range(ch+1,len(nums)):
                    if nums[i] % 2 == 0:
                        count +=1
                res.append(count)
            elif nums[ch] % 2 == 0:
                count = 0
                for i in range(ch+1,len(nums)):
                    if nums[i] % 2 != 0:
                        count += 1
                res.append(count)
            else:
                res.append(count)
        return res
