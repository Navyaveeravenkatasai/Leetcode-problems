class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score,reverse=True)
        freq={}
        for i in range(len(sorted_score)):
            if i == 0:
                freq[sorted_score[i]] = "Gold Medal"
            elif i == 1:
                freq[sorted_score[i]] = "Silver Medal"
            elif i == 2:
                freq[sorted_score[i]] = "Bronze Medal"
            else:
                freq[sorted_score[i]] = str(i+1)
        
        res=[]
        for s in score:
            res.append(freq[s])
        return res

