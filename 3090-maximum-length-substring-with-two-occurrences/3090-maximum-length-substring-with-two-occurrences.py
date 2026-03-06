class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count=[0] * 26
        res=left=0
        for i in range(0,len(s)):
            count[ord(s[i])-ord('a')] += 1
            while count[ord(s[i])-ord('a')] > 2:
                count[ord(s[left])-ord('a')] -= 1
                left+=1
            res=max(res,i-left+1)
        return res