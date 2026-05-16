class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        nums = list(set(nums))
        freq={}
        

        for ch in nums:
            if ch > 0:
                freq[ch] = freq.get(ch,0) + 1
        return len(freq)