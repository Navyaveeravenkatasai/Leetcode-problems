class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq={}
        maxi=0
        count=0
        for ch in nums:
            freq[ch] = freq.get(ch,0) + 1
        maxi=max(freq.values())
        for num in freq.values():
            if num == maxi:
                count+=1
        return maxi*count
