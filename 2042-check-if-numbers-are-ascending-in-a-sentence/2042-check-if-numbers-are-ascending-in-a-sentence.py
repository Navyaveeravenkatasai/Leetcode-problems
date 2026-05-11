class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        res=[]
        s=s.split()
        for ch in s:
            if ch.isdigit():
                res.append(int(ch))
        for ch in range(len(res)-1):
            if res[ch] >= res[ch+1]:
                return False
        return True