class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        res=[]
        for i in range(len(order)):
            if order[i] in friends:
                res.append(order[i])

        return res