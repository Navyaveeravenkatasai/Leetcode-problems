class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        freq={}
        for num in nums:
            freq[num] = freq.get(num,0) + 1


        pairs=0
        leftover=0
        for tot in freq.values():
            pairs += tot //2
            leftover += tot % 2
        return [pairs,leftover]