class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:

        maxi_res = []
        mini_res = []
        sumi = 0
        for ch in range(len(nums)):
            mini_res.append(nums[ch])

        for ch in range(len(nums)):
            maxi_res.append(nums[ch])
            res = max(maxi_res)
            ans = min(mini_res)

            sumi = res - ans

            if sumi <= k:
                return ch
            del mini_res[0]
        
        return -1
            