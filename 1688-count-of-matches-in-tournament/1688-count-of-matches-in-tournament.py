class Solution:
    def numberOfMatches(self, n: int) -> int:
        teams = n
        res=0
        while teams > 1:
            matches = teams //2
            res += matches
            advance = teams - matches
            teams = advance
        return res