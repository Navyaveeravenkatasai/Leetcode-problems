class Solution:
    def alternateDigitSum(self, n: int) -> int:
        even = 0
        odd = 0
        
        n = list(str(n))
        res =len(n)
        for ch in range(0,res,2):
            even += int(n[ch])
        
        for ch in range(1,res,2):
            odd += int(n[ch])
        return even - odd

