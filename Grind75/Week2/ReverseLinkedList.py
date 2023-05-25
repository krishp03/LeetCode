# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ReverseLinkedList:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        last = None
        curr = head

        while curr:
            tmp = curr.next
            curr.next = last
            last = curr
            curr = tmp

        return last
        
