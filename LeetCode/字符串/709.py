#!/usr/bin/env python
# encoding: utf-8
'''
@author: liuchang
@software: PyCharm
@file: 709.py
@time: 2020-07-07 09:00
'''
class Solution:
    def toLowerCase(self, str1):
        res = ""
        nDict = {'A':'a','B':'b','C':'c','D':'d','E':'e','F':'f','G':'g',
                 'H':'h','I':'i','J':'j','K':'k','L':'l','M':'m','N':'n',
                 'O':'o','P':'p','Q':'q','R':'r','S':'s','T':'t','U':'u',
                 'V':'v','W':'w','X':'x','Y':'y','Z':'z'}
        for i in range(len(str1)):
            if str1[i] in nDict.keys():
                res += nDict[str1[i]]
            else:
                res += str1[i]
        return res

s = Solution()
res = s.toLowerCase('Hello')
print(res)