from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = l1
        stringed1 = str(l1.val)
        while curr.next is not None:
            curr = curr.next
            stringed1 += str(curr.val)
        stringed1 = stringed1[::-1]
        stringed1_int = int(stringed1)
        curr = l2
        stringed2 = str(curr.val)
        while curr.next is not None:
            curr = curr.next
            stringed2 += str(curr.val)
        stringed2 = stringed2[::-1]
        stringed2_int = int(stringed2)
        result = stringed1_int + stringed2_int
        stringed_result = str(result)
        stringed_result = stringed_result[::-1]
        l3 = ListNode(val = int(stringed_result[0]))
        curr = l3
        for i in range(1, len(stringed_result)):
            curr.next = ListNode(val=int(stringed_result[i]))
            curr = curr.next
        return l3

if __name__ == "__main__":
    l1 = ListNode(val = 2, next = ListNode(val = 4, next = ListNode(val = 3)))
    l2 = ListNode(val = 5, next = ListNode(val = 6, next = ListNode(val = 4)))
    s = Solution()
    print(s.addTwoNumbers(l1, l2))