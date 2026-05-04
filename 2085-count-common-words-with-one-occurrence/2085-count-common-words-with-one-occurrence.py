class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        freq1={}
        freq2={}

        for ch in words1:
            freq1[ch] = freq1.get(ch,0) + 1

        for ch in words2:
            freq2[ch] = freq2.get(ch,0) + 1

        count = 0

        for word in freq1:
            if freq1[word] == 1 and freq2.get(word,0) == 1:
                count +=1
        return count 