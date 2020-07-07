#!/usr/bin/env python
# encoding: utf-8
'''
@author: liuchang
@software: PyCharm
@file: 917.py
@time: 2020-07-07 09:19
'''
class Solution:
    def reverseOnlyLetters(self, S):
        a = []
        b = {}
        for i, c in enumerate(S):
            if c.isalpha():
                a.insert(0, c)
            else:
                b[i] = c
        for i, c in b.items():
            a.insert(i, c)
        return ''.join(a)


s = Solution()
res = s.reverseOnlyLetters("ab-cd")
print(res)
