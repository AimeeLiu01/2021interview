#!/usr/bin/env python
# encoding: utf-8
'''
@author: liuchang
@software: PyCharm
@file: LinkNode.py
@time: 2020-07-30 23:17
'''
class LinkNode(object):

    value = 0
    next = None
    def __init__(self,v,n):
        self.value = v
        self.next = n

    def hasNext(self):
        return next is not None


    def print_list(self):
        output = str(self.value)
        node = self
        while node.next is not None:
            node = node.next
            output += "->" + str(node.value)
        return output


    def reverseList(self):
        head = self
        pre = None
        while head:
            temp = head
            head = head.next
            temp.next = pre
            pre = temp
        return pre





if __name__ == '__main__':
    node1 = LinkNode(5, None)
    node2 = LinkNode(3, node1)
    node3 = LinkNode(1, node2)
    print(node2.value)
    print(node2.next.value)
    print(node3.print_list())
    print(node3.reverseList().print_list())

