# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head == None:
            return head
        temp = head
        while head.val == val:
            head = head.next
            if head == None:
                return head
        while(temp != None):
            if temp.next!=None and temp.next.val == val:
                t = temp.next.next
                temp.next = t
            else:
                temp = temp.next
        return head
