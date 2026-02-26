from collections import defaultdict
from typing import List
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res=0
        numbers = defaultdict(int)
        for num in nums:
            res += numbers[num]
            numbers[num] += 1
        return res

