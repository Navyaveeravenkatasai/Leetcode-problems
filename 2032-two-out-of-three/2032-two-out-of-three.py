class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        
        s1 = set(nums1)
        s2 = set(nums2)
        s3 = set(nums3)

        res= []

        for num in s1 | s2 | s3:
            count = 0

            if num in s1:
                count += 1
            if num in s2:
                count += 1
            if num in s3:
                count += 1

            if count >= 2:
                res.append(num)

        return res