class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        freq={}
        res=[]
        for num in nums:
            freq[num] = freq.get(num,0) + 1
        
        for key in freq:
            if freq[key] == 2:
                res.append(key)
        return res
