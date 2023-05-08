class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        if not head.next:
            return None

        dummy = ListNode(0, head)
        fast, slow = dummy, dummy
        while n >= 0 and fast:
            n -= 1
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head
