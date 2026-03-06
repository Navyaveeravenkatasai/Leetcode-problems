class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq={}
        res=left=0
        for ch  in range(0,len(s)):
            freq[ch] = freq.get(ch,0) + 1
            
            while freq[ch] > 2:
                left_char = s[left]
                freq[left_char] -= 1
                left+=1
            res=max(res,ch-left+1)
        return res // 2