class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        res = startTime.split(':')
        res1 = endTime.split(':')
        
        tot = 0
        count = 0

        for ch in range(len(res)):
            if ch == 0:
                tot += int(res[ch]) * 3600
            elif ch == 1:
                tot += int(res[ch]) * 60
            elif ch == 2:
                tot += int(res[ch])

        for ch in range(len(res1)):
            if ch == 0:
                count += int(res1[ch]) * 3600
            elif ch == 1:
                count += int(res1[ch]) * 60
            elif ch == 2:
                count += int(res1[ch])
        return count - tot
