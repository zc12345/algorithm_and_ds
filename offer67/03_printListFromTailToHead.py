'''
输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
'''
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        res = []
        while listNode:
            res.append(listNode.val)
            listNode = listNode.next
        return res[::-1]

class Solution2:
    # 递归的方法
    def printListFromTailToHead(self, listNode):
        # write code here
        res = []
        def printNode(listNode):
            if listNode:
                printNode(listNode.next)
                res.append(listNode.val)
        printNode(listNode)
        return res

if __name__ == "__main__":
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l1.next = l2
    l2.next = l3
    res = Solution().printListFromTailToHead(l1)
    print(res)