# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head
        res=set()

        while temp is not None:
            if temp in res:
                return True
            res.add(temp)
            temp=temp.next
        return False
