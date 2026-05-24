
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = head
        arr=[]

        while temp:
            arr.append(temp.val)
            temp = temp.next

        return arr == arr[::-1]