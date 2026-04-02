class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res=[]

        for ch in words:
            temp=0
            for i in ch:
                temp += weights[ord(i) - ord('a')]
            res.append(chr(ord('z') - (temp % 26)))
        return ''.join(res)