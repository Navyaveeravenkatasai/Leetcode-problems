class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        alice=0
        bob=alice+1
        res=[]
        for i in range(0,len(nums)-1,2):
            alice=nums[i]
            bob=nums[i+1]
            res.append(bob)
            res.append(alice)
        return res