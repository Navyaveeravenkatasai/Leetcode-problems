class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        n=len(arr)
        mini_diff= float('inf')
        res=[]

        for i in range(len(arr)-1):
            curr_diff=arr[i+1]-arr[i]
            if curr_diff < mini_diff:
                mini_diff = curr_diff
                res = [[arr[i] ,arr[i+1]]]
            elif curr_diff == mini_diff:
                res.append([arr[i],arr[i+1]])
        return res
