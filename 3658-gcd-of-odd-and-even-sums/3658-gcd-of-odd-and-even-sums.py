from math import gcd
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        even = []
        odd = []
        count = 0
        odd_number = [num for num in range(1, n*2, 2)]
        even_number = [num for num in range(2, (n*2)+1, 2)]
        tot = gcd(sum(even_number),sum(odd_number))
        return tot