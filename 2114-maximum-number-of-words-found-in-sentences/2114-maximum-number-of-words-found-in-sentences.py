class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxi=0

        for i in sentences:
            words=i.split()
            n=len(words)
            maxi=max(maxi,n)
        return maxi