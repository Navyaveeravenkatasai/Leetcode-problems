class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter=defaultdict(int)
        balloon='balloon'

        for ch in text:
            if ch in balloon:
                counter[ch] +=1
        if any(ch not in counter for ch in balloon):
            return 0
        else:
            return min(counter['b'],counter['a'],counter['l']//2,counter['o']//2,counter['n'])
