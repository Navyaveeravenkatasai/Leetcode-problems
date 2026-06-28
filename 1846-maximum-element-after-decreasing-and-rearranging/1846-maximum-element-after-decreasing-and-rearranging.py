class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        res = []
        arr.sort()
        count = 1
        res.append(count)

        for ch in range(1,len(arr)):
            if arr[ch] >= count + 1:
                count += 1
                
            res.append(count)
        return max(res)
            
