# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        p, q, curr = l1, l2, dummy
        carry = 0
        
        while p or q:
            x = p.val if p else 0
            y = q.val if q else 0
            s = x + y + carry
            carry = s // 10
            curr.next = ListNode(s % 10)
            curr = curr.next
            if p:
                p = p.next
            
            if q:
                q = q.next
        
        if carry > 0:
            curr.next = ListNode(carry)
        
        return dummy.next