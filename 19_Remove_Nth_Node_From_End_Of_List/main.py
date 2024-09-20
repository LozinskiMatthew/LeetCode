from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        if curr.next is None:
            head = None
            return head
        counter = 1
        curr = head
        while curr.next is not None:
            curr = curr.next
            counter += 1
        curr = head
        if counter == n:
            head = head.next
            return head
        counter -= n
        k = 1
        while True:
            if k == counter:
                curr.next = curr.next.next
                break
            if curr.next is None:
                break
            curr = curr.next
            k += 1
        return head