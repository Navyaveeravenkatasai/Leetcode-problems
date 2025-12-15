class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def mergeSort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])

            return merge(left, right)

        def merge(a, b):
            i = j = 0
            res = []
            while i < len(a) and j < len(b):
                if a[i] <= b[j]:
                    res.append(a[i]); i += 1
                else:
                    res.append(b[j]); j += 1
            return res + a[i:] + b[j:]

        return mergeSort(nums)