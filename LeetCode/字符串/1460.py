#!/usr/bin/env python
# encoding: utf-8
'''
@author: liuchang
@software: PyCharm
@file: 1460.py
@time: 2020-07-07 08:49
'''

class Solution:
    def canBeEqual(self, target, arr):
        ndict = {}
        ndict2 = {}
        for i in range(len(target)):
            if target[i] not in ndict:
                ndict[target[i]] = 1
            else:
                ndict[target[i]] += 1
        for i in range(len(arr)):
            if arr[i] not in ndict2:
                ndict2[arr[i]] = 1
            else:
                ndict2[arr[i]] += 1
        return ndict2 == ndict

s = Solution()
res = s.canBeEqual([1,1,3,4], [2,3,4,1])
print(res)
