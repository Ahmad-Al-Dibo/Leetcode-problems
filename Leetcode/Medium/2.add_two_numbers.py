class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_linked(lst):
    dummy = ListNode()
    current = dummy
    for v in lst:
        current.next = ListNode(v)
        current = current.next
    return dummy.next


def linked_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next

anser = Solution().addTwoNumbers(list_to_linked([2,4,3]), list_to_linked([5,6,4]))
print(linked_to_list(anser))


"""
input 1
l1 = [2,4,3]
l2 = [5,6,4]
Output 1
[7,0,8]
Expected 1
[7,0,8]

Input 2
l1 =
[0]
l2 =
[0]
Output 2
[0]
Expected 2
[0]


Input 3
l1 =
[9,9,9,9,9,9,9]
l2 =
[9,9,9,9]
Output 3
[8,9,9,9,0,0 0,1]
Expected 3
[8,9,9,9,0,0,0,1]
"""
