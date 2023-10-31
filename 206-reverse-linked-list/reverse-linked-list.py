# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None

        def _helper(head, prev):
            if head is None:
                return prev

            next = head.next
            head.next = prev
            return _helper(next, head)

        return _helper(head, prev)
        