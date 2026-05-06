class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        res=[]
        for ch in range(1,len(nums)):
            totalsum = nums[ch-1] + nums[ch]
            res.append(totalsum)

        freq={}

        for ch in res:
            freq[ch] = freq.get(ch,0) + 1

        for key in freq.values():
            if key > 1:
                return True
        return False