#!/usr/bin/env python
# encoding: utf-8
'''
@author: liuchang
@software: PyCharm
@file: 206.py
@time: 2020-07-15 14:22
'''
# Definition for singly-linked list.

class Node(object):
    '''
    节点类
    '''
    def __init__(self, data):
        self.num = data
        self.next = None

class DeleteNode():
    '''
    实现删除指定节点功能
    '''
    def delete_node(self, node):
        node.num = node.next.num
        node.next = node.next.next

class ReverseNode():
    def reverseList(self, head):
        pre = None
        cur = head
        while cur:
            temp = cur.next   # 先把原来cur.next位置存起来
            cur.next = pre
            pre = cur
            cur = temp
        return pre

class PrintNode():
    '''
    输出指定节点为起始节点的链表
    '''
    def print_node(self, node):
        res_list = []
        while node:
            res_list.append(str(node.num))
            node = node.next
        print('->'.join(res_list))


if __name__ == '__main__':
    node1 = Node(90)
    node2 = Node(34)
    node3 = Node(89)
    node4 = Node(77)
    node5 = Node(23)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    print('init single linknode is:')
    printnode = PrintNode()
    printnode.print_node(node1)

    delete = DeleteNode()
    delete.delete_node(node4)
    print('after delete node,the single linknode is:')
    printnode.print_node(node1)

    reversenode = ReverseNode()
    print('after reverse node, the single linknode is: ')
    nodeN = reversenode.reverseList(node1)
    printnode.print_node(nodeN)

