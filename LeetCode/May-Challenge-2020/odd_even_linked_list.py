# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if(head == None or head.next == None):
            return head
        odd = head
        even = head.next
        e = even
        while(even != None and even.next != None):
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = e
        return head
