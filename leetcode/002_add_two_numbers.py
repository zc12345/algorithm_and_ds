# coding=utf8
'''
2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
def num2ListNode(numbers):
    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next
    ptr = dummyRoot.next
    return ptr

def listNode2String(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

class Solution1:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        digit = 0
        carry = 0
        result = ListNode(0)
        pointer = result
        
        while l1 or l2 or carry:
            carry, digit = divmod((carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)) , 10)
            pointer.next = ListNode(digit)
            pointer = pointer.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return result.next

class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        digit = 0
        carry = 0
        result = ListNode(0)
        pointer = result
        
        while l1 or l2:
            carry, digit = divmod((carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)) , 10)
            pointer.next = ListNode(digit)
            pointer = pointer.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry:
            pointer.next = ListNode(1)
            
        return result.next

class Solution3:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = 0
        b = 0
        m = 1
        n = 1
        while l1:
            a += l1.val*m
            l1 = l1.next
            m = m * 10
        while l2:
            b += l2.val*n
            l2 = l2.next
            n = n *10
        c = a + b
        c = str(c)
        l = ListNode(0)
        l3 = l
        for i,s in enumerate(reversed(c)):
            l3.next = ListNode(int(s))
            l3 = l3.next
        return l.next

class Solution4:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        digit = 0
        carry = 0
        result = ListNode(0)
        pointer = result
        
        while l1 or l2 or not (carry == 0):
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            tmp = carry + num1 + num2
            digit = tmp % 10
            carry = tmp // 10
            pointer.next = ListNode(digit)
            pointer = pointer.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return result.next

    
if __name__ == '__main__':
    a = [2, 4, 3]
    b = [5, 6, 4]
    a = num2ListNode(a)
    b = num2ListNode(b) 
    res = Solution4().addTwoNumbers(a, b)
    print(listNode2String(res))
