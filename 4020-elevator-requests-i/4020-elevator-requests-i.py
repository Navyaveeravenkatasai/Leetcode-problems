class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        count = requests[0]

        for i in range(1,len(requests)):
            res =0
            if requests[i] < requests[i-1]:
                res = requests[i-1] - requests[i]
                count += res
            elif requests[i] > requests[i-1]:
                res = requests[i] - requests[i-1]
                count += res
            elif requests[i] == requests[i-1]:
                continue
        
        return count