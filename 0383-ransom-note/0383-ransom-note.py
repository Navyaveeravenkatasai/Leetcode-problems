class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter={}
        for ch in magazine:
            if ch in counter:
                counter[ch] +=1
            else:
                counter[ch] = 1
            
        for ch in ransomNote:
            if ch not in counter:
                return False
            elif counter[ch] == 1:
                del counter[ch]
            else:
                counter[ch] -=1
        return True