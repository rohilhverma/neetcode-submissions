# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:  

    def m(self, l1, l2):
        dummy=ListNode(0,None)
        returnDummy=dummy
        while l1 and l2:
            if l1.val <= l2.val:
                dummy.next=l1
                dummy=dummy.next
                l1=l1.next
            else:
                dummy.next=l2
                dummy=dummy.next
                l2=l2.next
        if l1:
            dummy.next = l1
        elif l2:
            dummy.next=l2
        return returnDummy.next


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if len(lists)==0:
            return None
        elif len(lists) ==1:
            return lists[0]
        
        merged=self.m(lists[0],lists[1])
    
        for x in range(2,len(lists)):
            merged=self.m(merged,lists[x])

        return merged
