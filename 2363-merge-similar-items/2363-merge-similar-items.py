class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        freq={}

        for value, weight in items1:
            freq[value] = freq.get(value,0) + weight

        for value , weight in items2:
            freq[value] = freq.get(value,0) + weight

        res= []

        for value in sorted(freq):
            res.append([value,freq[value]])
        
        return res