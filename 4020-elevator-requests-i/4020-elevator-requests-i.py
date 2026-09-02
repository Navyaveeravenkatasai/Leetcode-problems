class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        res = 0
        for i in range(1,len(requests)):
            res += abs(requests[i-1] - requests[i])
        return res + requests[0]