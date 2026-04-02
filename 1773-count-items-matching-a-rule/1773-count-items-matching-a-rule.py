class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        freq =  { "type": 0 , "color" : 1 , "name" : 2}
        count = 0
        for ch in items:
            if ch[freq[ruleKey]] == ruleValue :
                count += 1

        return count