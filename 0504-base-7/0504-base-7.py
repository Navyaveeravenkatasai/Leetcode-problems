import numpy as np
class Solution:
    def convertToBase7(self, num: int) -> str:
        res = np.base_repr(num , 7)
        return str(res)
        