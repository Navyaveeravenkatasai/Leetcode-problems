# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
            def find_len(linkedlist):
                length = 0
                while linkedlist:
                    length += 1
                    linkedlist = linkedlist.next
                return length
            len_headA = find_len(headA)
            len_headB = find_len(headB)

            while len_headA > len_headB:
                headA = headA.next
                len_headA -= 1
            
            while len_headB > len_headA:
                headB = headB.next
                len_headB -= 1

            while headA != headB:
                headA = headA.next
                headB = headB.next
            
            return headA

            

