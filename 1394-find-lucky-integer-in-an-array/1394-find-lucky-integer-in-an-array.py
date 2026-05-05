class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq={}
        count = 0
        for ch in arr:
            freq[ch] = freq.get(ch,0) + 1

        res=[]
        maxi=-1

        for key,value in freq.items():
            if key == value:
                maxi=max(maxi,key)
        return maxi