class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        freq = {}
        res = []

        for ch in nums:
            freq[ch] = freq.get(ch,0) + 1

        for key,value in freq.items():
            if value == 1 and key % 2 == 0:
                res.append(key)

        for ch in res:
            return res[0] 
        return -1