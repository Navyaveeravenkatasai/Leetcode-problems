class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        
        temp = head
        n = 0

        while temp is not None:
            n += 1
            temp = temp.next

        temp = head
        res = 0

        for i in range(n - 1, -1, -1):
            res += temp.val * (2 ** i)
            temp = temp.next

        return res