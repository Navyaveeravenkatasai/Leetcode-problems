class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk=[]
        for num in operations:
            if num == '+':
                stk.append(stk[-1] + stk[-2])
            elif num == 'D':
                stk.append(stk[-1] * 2)
            elif num == 'C':
                stk.pop()
            else:
                stk.append(int(num))
        return sum(stk)