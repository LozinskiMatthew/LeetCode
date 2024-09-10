class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def lesser(self, a: int, b: int):
        if a < b:
            return a, b
        else:
            return b, a

    def divisors(self, a: int) -> List[int]:
        divisors = []
        for i in range(1, a + 1):
            if a % i == 0:
                divisors.append(i)
        return divisors

    def biggest_divisor(self, a, b: List[int]):
        biggest = 1
        for num in b:
            if a % num == 0:
                biggest = num
        return biggest


    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr.next != None:
            a = curr.val
            b = curr.next.val
            lesser, bigger = self.lesser(a, b)
            divs = self.divisors(lesser)
            bigdiv = self.biggest_divisor(bigger, divs)
            new_node = ListNode(val=bigdiv)
            new_node.next = curr.next
            curr.next = new_node
            curr = curr.next.next
        return head