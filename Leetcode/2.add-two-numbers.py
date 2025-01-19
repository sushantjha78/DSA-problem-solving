#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        totals_digits = []
        while (l1.next and l2.next):
            total = l1.val + l2.val + carry
            totals_digits.append(total%10)
            carry = total // 10
            l1 = l1.next
            l2 = l2.next

        while (l1.next or l2.next):
            if l1.next != None:
                total = l1.val + carry
                totals_digits.append(total%10)
                carry = total // 10
                l1 = l1.next

            elif l2.next != None:
                total = l2.val + carry
                totals_digits.append(total%10)
                carry = total // 10
                l2 = l2.next

        if carry != 0:
            totals_digits.append(carry)

        return totals_digits







# @lc code=end

