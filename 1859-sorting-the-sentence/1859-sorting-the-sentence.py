class Solution:
    def sortSentence(self, s: str) -> str:
        s =  s.split(' ')
        s.sort(key = lambda x:x[-1])

        result = " ".join(word[:-1] for word in s)
        return result