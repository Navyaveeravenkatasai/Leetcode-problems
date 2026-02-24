class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        
        even = 0   # even index pointer
        odd = 1    # odd index pointer
        n = len(nums)
        
        while even < n and odd < n:
            
            # if even index has odd number
            if nums[even] % 2 != 0:
                
                # find an even number at odd index
                while nums[odd] % 2 != 0:
                    odd += 2
                
                # swap
                nums[even], nums[odd] = nums[odd], nums[even]
            
            even += 2
        
        return nums