class Solution:
    def minimizedStringLength(self, s: str) -> int:
        s=list(s)
        freq={}
        for ch in s:
            freq[ch] = freq.get(ch,0) + 1
        count = 0
        for key in freq.values():
            if key > 1:
                count +=1
            elif key == 1:
                count +=1
        return count