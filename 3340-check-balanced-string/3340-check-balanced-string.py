class Solution:
    def isBalanced(self, num: str) -> bool:
        num = list(num)
        evenres = 0
        oddres = 0

        for i in range(len(num)):
            if i % 2 == 0:
                evenres += int(num[i])
            else:
                oddres += int(num[i])

        if evenres == oddres:
            return True
        return False
