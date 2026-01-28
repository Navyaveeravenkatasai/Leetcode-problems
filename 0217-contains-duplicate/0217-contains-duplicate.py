class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s=set()
        for ch in nums:
            if ch in s:
                return True
            else:
                s.add(ch)
        return False
