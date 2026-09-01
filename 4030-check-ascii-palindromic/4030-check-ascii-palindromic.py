class Solution:
    def isPalindromic(self, s: str) -> bool:
        s = list(s)
        res = ''.join(bin(ord(ch))[2:].zfill(8) for ch in s)
        res = list(res)
        left = 0
        right =len(res)-1 

        while left < right:
            if res[left] != res[right]:
                return False
            left += 1
            right -= 1
        return True