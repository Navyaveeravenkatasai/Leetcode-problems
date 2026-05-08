class Solution:
    def balancedStringSplit(self, s: str) -> int:
        rightcount =  0
        count = 0
        for ch in s:
            if ch == 'R':
                rightcount += 1
            elif ch == 'L':
                rightcount -= 1
            if rightcount == 0:
                count += 1
        return count

