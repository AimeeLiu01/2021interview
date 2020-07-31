#!/usr/bin/env python
# encoding: utf-8
'''
@author: liuchang
@software: PyCharm
@file: 两个链表的第一个公共节点.py
@time: 2020-07-31 09:33
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def print_list(self):
        output = str(self.val)
        node = self
        while node.next is not None:
            node = node.next
            output += "->" + str(node.val)
        return output


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        nLength1 = self.GetListLength(pHead1)
        nLength2 = self.GetListLength(pHead2)
        nLengthDiff = abs(nLength1 - nLength2)

        if nLength1 > nLength2:
            pListHeadLong = pHead1
            pListHeadShort = pHead2
        else:
            pListHeadLong = pHead2
            pListHeadShort = pHead1

        for i in range(nLengthDiff):
            pListHeadLong = pListHeadLong.next

        while pListHeadLong != None and pListHeadShort != None and pListHeadLong != pListHeadShort:
            pListHeadLong = pListHeadLong.next
            pListHeadShort = pListHeadShort.next

        pFirstCommonNode = pListHeadLong
        return pFirstCommonNode


    def GetListLength(self, pHead):
        nLength = 0
        while pHead != None:
            pHead = pHead.next
            nLength += 1
        return nLength


if __name__ == '__main__':
    pHead1 = ListNode(1)
    pHead2 = ListNode(3)
    pHead3 = ListNode(5)
    pHead4 = ListNode(7)

    pHead1.next = pHead2
    pHead2.next = pHead3
    pHead3.next = pHead4

    s = Solution()
    res = s.FindFirstCommonNode(pHead1, pHead3)
    print(res.print_list())

