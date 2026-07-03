class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0

        for ch in range(2,len(arr)):
            if arr[ch] % 2 != 0 and arr[ch-1] % 2 != 0 and arr[ch-2] % 2 != 0:
                count = 1
                
        if count == 1:
            return True
        return False