class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq={}
        res=left=0
        for right  in range(0,len(s)):
            ch=s[right]
            freq[ch] = freq.get(ch,0) + 1
            
            while freq[ch] > 2:
                left_char = s[left]
                freq[left_char] -= 1
                left+=1
            res=max(res,right-left+1)
        return res