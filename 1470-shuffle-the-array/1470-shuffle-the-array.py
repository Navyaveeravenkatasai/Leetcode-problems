class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res=[]
        low = 0
        high = len(nums)-1
        mid = (low+high) // 2
        while low < mid and mid < high:
            res.append(nums[low])
            res.append(nums[mid+1])
            low+=1
            mid+=1
        return res