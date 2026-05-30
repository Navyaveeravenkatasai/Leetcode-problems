class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        res=[]
        n=len(arr)

        for ch in arr:
            if ch == 0:
                res.append(0)
                res.append(0)
            else:
                res.append(ch)

        for i in range(n):
            arr[i] = res[i]