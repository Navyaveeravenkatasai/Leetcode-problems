class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        zero=0
        one=0
        left=0
        count=0

        for right in range(len(s)):
            if s[right] == '0':
                zero +=1
            else:
                one += 1

            while zero > k  and one > k:
                if s[left] == '0':
                    zero -= 1
                else:
                    one -=1
                left += 1
            count += right - left + 1
        return count