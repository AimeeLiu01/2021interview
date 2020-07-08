#!/usr/bin/env python
# encoding: utf-8
'''
@author: liuchang
@software: PyCharm
@file: 17.py
@time: 2020-07-08 15:43
'''
class Solution:
    def multiSearch(self, big, smalls):
        res = []
        for s in smalls:
            if not s:
                res.append([])
                continue
            tmp = []
            j = big.find(s)
            while j >= 0:
                tmp.append(j)
                j = big.find(s, j+1)
            res.append(tmp)
        return res

big = "mississippi"
smalls = ["is","ppi","hi","sis","i","ssippi"]
s = Solution()
res = s.multiSearch(big, smalls)
print(res)
