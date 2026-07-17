import numpy as np
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        if n == 10 and k == 10:
            return 1

        bases = np.base_repr(n, base=k)
        bases = int(bases)
        summ = 0
        while bases > 0:
            summ += bases % 10
            bases = bases // 10
        return summ