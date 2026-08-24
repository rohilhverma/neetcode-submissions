# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = ListNode()
        lst3 = list3
        while (list1 != None and list2 != None):
            if (list1.val <= list2.val):
                lst3.next = ListNode(list1.val)
                list1 = list1.next
            else:
                lst3.next = ListNode(list2.val)
                list2 = list2.next
            lst3 = lst3.next
        if list1:
            lst3.next = list1
        if list2:
            lst3.next = list2
        return list3.next
            