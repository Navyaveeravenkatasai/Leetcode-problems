class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        freq1={}
        freq2={}

        for ch in nums1:
            freq1[ch] = freq1.get(ch,0)+1
        
        for i in nums2:
            freq2[i] = freq2.get(i,0)+1

        common=[]
        for key in freq1:
            if key in freq2:
                common.append(key)
        
        if common:
            return min(common)
        return -1
        
