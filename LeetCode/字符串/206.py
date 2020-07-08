#!/usr/bin/env python
# encoding: utf-8
'''
@author: liuchang
@software: PyCharm
@file: 206.py
@time: 2020-07-08 15:29
'''
class Solution:
    def singleNumber(self, nums):
        res = []
        ndict = {}
        for i in range(len(nums)):
            if nums[i] not in ndict.keys():
                ndict[nums[i]] = 1
            elif nums[i] in ndict.keys():
                ndict[nums[i]] += 1

        for item in ndict.keys():
            if ndict[item] == 1:
                res.append(item)
        return res

s = Solution()
res = s.singleNumber([1,2,1,3,2,5])
print(res)


