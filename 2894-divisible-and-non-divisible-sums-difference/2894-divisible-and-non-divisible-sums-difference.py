class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        divide = []
        error = []
        for ch in range(1,n+1):
            if ch % m == 0:
                divide.append(ch)
            else:
                error.append(ch)
        return sum(error) - sum(divide)