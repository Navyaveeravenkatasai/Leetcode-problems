class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        
        # Start with frequency of first word
        freq = {}
        for ch in words[0]:
            freq[ch] = freq.get(ch, 0) + 1
        
        # Compare with remaining words
        for i in range(1, len(words)):
            temp = {}
            for ch in words[i]:
                temp[ch] = temp.get(ch, 0) + 1
            
            # take minimum frequency
            for ch in list(freq.keys()):
                if ch in temp:
                    freq[ch] = min(freq[ch], temp[ch])
                else:
                    del freq[ch]
        
        # build result
        for ch in freq:
            res.extend([ch] * freq[ch])
        
        return res