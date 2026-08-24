# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        def help(l1,l2):
            returnNode =dummy=ListNode(None, None)
            while l1 and l2:
                if l1.val < l2.val:
                    dummy.next = ListNode(l1.val, None)
                    l1 = l1.next
                else:
                    dummy.next = ListNode(l2.val, None)
                    l2 = l2.next
                dummy = dummy.next
            if l1:
                dummy.next=l1
            if l2:
                dummy.next=l2
            
            return returnNode.next


        while len(lists) > 1:
            x, y = lists.pop(0), lists.pop(0)
            lists.append(help(x, y))

        return lists[0]
                
        