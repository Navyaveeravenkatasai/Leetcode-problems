class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        ans = 0
        for ch in nums:
            if ch == 1:
                count +=1
            else:
                count = 0

            ans = max(ans,count)
        return ans
            

            
