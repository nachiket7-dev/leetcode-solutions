# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        h1 = list1
        h2 = list2
        head = None
        if h1 is None:
            return h2
        elif h2 is None:
            return h1
        if h1.val < h2.val:
            head = ListNode(h1.val)
            h1 = h1.next
        else:
            head = ListNode(h2.val)
            h2 = h2.next
        tail = head
        while h1 and h2:
            if h1.val < h2.val:
                node = ListNode(h1.val)
                tail.next = node
                tail = tail.next
                h1 = h1.next
            else:
                node = ListNode(h2.val)
                tail.next = node
                tail = tail.next
                h2 = h2.next
        if h1:
            while h1:
                tail.next = ListNode(h1.val)
                tail = tail.next
                h1 = h1.next
        else:
            while h2:
                tail.next = ListNode(h2.val)
                tail = tail.next
                h2 = h2.next
        return head
            