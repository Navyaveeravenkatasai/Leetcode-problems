class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxiAltitude=0
        currentAltitude = 0
        for i in range(len(gain)):
            currentAltitude = currentAltitude + gain[i]
            maxiAltitude = max(maxiAltitude,currentAltitude)
        return maxiAltitude