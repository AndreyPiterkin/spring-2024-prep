class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next   
        

        original_start, reversed_start = head, prev
        while reversed_start.next:
            original_start.next, original_start = reversed_start, original_start.next
            reversed_start.next, reversed_start = original_start, reversed_start.next

