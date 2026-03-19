class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq={}
        for char in t:
            freq[char] = freq.get(char,0)+1
        
        for ch in s:
            freq[ch] -=1
            if freq[ch] == 0:
                del freq[ch]

        return list(freq.keys())[0]