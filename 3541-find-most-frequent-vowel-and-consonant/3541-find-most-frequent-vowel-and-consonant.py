class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels={'a','e','i','o','u'}
        count=0
        freq={}
        vowelmax=0
        consonantmax=0
        for ch in s:
            freq[ch]=freq.get(ch,0) + 1
        
        for i in freq:
            if i in vowels:
                vowelmax=max(freq[i],vowelmax)
            elif i not in vowels:
                consonantmax=max(freq[i],consonantmax)
        
        count = vowelmax + consonantmax

        return count

