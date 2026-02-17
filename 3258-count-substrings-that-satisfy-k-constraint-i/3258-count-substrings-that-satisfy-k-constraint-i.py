class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        zero_count = 0
        ones_count = 0
        left = 0
        count = 0
        
        for right in range(len(s)):
            if s[right] == '0':
                zero_count += 1
            else:
                ones_count += 1
            
            while zero_count > k and ones_count > k:
                if s[left] == '0':
                    zero_count -= 1
                else:
                    ones_count -= 1
                left += 1
            
            count += right - left + 1
        
        return count
