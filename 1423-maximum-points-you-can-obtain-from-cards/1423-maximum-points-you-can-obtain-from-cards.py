class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)

        if n == k:
            return sum(cardPoints)
        
        leftsum, rightsum = 0,0

        for i in range(0,k):
            leftsum += cardPoints[i]

        maxi = leftsum
        rightind = n-1

        for i in range(k-1,-1,-1):
            leftsum -= cardPoints[i]
            rightsum += cardPoints[rightind]
            maxi = max(maxi,leftsum+rightsum)
            rightind -= 1
        return maxi
