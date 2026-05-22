# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        curr = head.next

        while curr:
            gcd =  math.gcd(curr.val,temp.val)
            g = ListNode(gcd)
            temp.next = g
            g.next = curr
            temp = curr
            curr = curr.next

        return head