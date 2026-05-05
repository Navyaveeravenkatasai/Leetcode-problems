from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = []
        count = 0

        for ch in words:
            temp = list(chars)   
            valid = True

            for i in ch:
                if i in temp:
                    temp.remove(i)
                else:
                    valid = False
                    break
            
            if valid:
                res.append(ch)

        for word in res:
            count += len(word)

        return count