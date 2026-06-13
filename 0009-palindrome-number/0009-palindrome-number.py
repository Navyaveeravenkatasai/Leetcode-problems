class Solution:
    def isPalindrome(self, x: int) -> bool:
        x= list(str(x))

        rev = x[::-1]

        return rev == x
                