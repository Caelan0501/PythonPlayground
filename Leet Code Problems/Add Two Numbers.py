'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def readList(l):
    multiplier = 1
    a = 0
    while l is not None:
        i = l.val * multiplier
        a = a + i
        multiplier = multiplier * 10
        l = l.next
    return a

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        sum = readList(l1) + readList(l2)
        rlist = ListNode()
        curr = rlist
        while sum != 0:
            curr.val = sum % 10
            sum = sum // 10
            if sum != 0:
                curr.next = ListNode()
                curr = curr.next
        return rlist