# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        if head is None:
            return None
        i = head
        count = 0
        while i:
            i = i.next
            count += 1
        if n > count:
            return head
        a = count - n
        if a == 0:
            return head.next
        j = head
        if a == 0:
            j.next = head
        while a > 1:
            j = j.next
            a -= 1
        if j.next != None:
            j.next = j.next.next
        return head