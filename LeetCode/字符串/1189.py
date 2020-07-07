#!/usr/bin/env python
# encoding: utf-8
'''
@author: liuchang
@software: PyCharm
@file: 1189.py
@time: 2020-07-07 09:33
'''


class Solution:
    def maxNumberOfBalloons(self, text):
        a = ['b', 'a', 'l', 'o', 'n']
        ndict = {}
        for i in range(len(text)):
            if text[i] in a and text[i] not in ndict.keys():
                ndict[text[i]] = 1
            elif text[i] in a and text[i] in ndict.keys():
                ndict[text[i]] += 1
        if 'o' in ndict.keys():
            ndict['o'] = ndict['o']/2
        if 'l' in ndict.keys():
            ndict['l'] = ndict['l']/2
        for item in a:
            if item not in ndict.keys():
                return 0
        min = 9999
        for i in ndict.keys():
            if ndict[i] < min:
                min = ndict[i]
        return int(min)


s = Solution()
res = s.maxNumberOfBalloons('lloo')
print(res)
