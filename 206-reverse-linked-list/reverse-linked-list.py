# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        i = head
        lst = []
        while i:
            if i.next is None:
                lst.append(i.val)
                break
            lst.append(i.val)
            i = i.next
        if not lst:
            return None
        lst.reverse()
        n = ListNode(lst[0])
        m = n
        for i in range(1,len(lst)):
            print(lst[i])
            n.next = ListNode(lst[i])
            n = n.next
        return m
            