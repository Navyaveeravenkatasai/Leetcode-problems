from typing import List

class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words:
            return -1
        
        n = len(words)
        min_steps = float('inf')
        
        for i in range(n):
            if words[i] == target:
                steps = min(abs(i - startIndex), n - abs(i - startIndex))
                min_steps = min(min_steps, steps)
        
        return min_steps