# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carryVal = 0
        dummyNode = ListNode(0, None)
        y = dummyNode
        while l1 and l2:
            if (l1.val + l2.val + carryVal <= 9):
                value = l1.val + l2.val + carryVal
                carryVal = 0
            else:
                value = (l1.val + l2.val + carryVal) % 10
                carryVal = (l1.val + l2.val + carryVal) // 10
            y.next = ListNode(value, None)
            l1 = l1.next
            l2 = l2.next
            y = y.next
        while l1:
            if (l1.val + carryVal <= 9):
                value = l1.val + carryVal
                carryVal = 0
            else:
                value = (l1.val + carryVal) % 10
                carryVal = (l1.val + carryVal) // 10
            y.next = ListNode(value, None)
            l1 = l1.next
            y=y.next
        while l2:
            if (l2.val + carryVal <= 9):
                value = l2.val + carryVal
                carryVal = 0
            else:
                value = (l2.val + carryVal) % 10
                carryVal = (l2.val + carryVal) // 10
            y.next = ListNode(value, None)
            l2 = l2.next
            y=y.next
        if carryVal:
            y.next = ListNode(carryVal, None)
        return dummyNode.next


