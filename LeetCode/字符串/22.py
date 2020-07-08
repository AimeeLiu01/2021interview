#!/usr/bin/env python
# encoding: utf-8
'''
@author: liuchang
@software: PyCharm
@file: 22.py
@time: 2020-07-08 14:54
'''
"""
回溯法的代码套路是使用两个变量： res 和 path，res 表示最终的结果，
path 保存已经走过的路径。如果搜到一个状态满足题目要求，就把 path 放到 res 中。
链接：https://leetcode-cn.com/problems/generate-parentheses/solution/ru-men-ji-bie-de-hui-su-fa-xue-hui-tao-lu-miao-don/
"""
class Solution:
    def generateParenthesis(self, n):
        res = []
        self.dfs(res, n, n, '')
        return res

    def dfs(self, res, left, right, path):
        if left == 0 and right == 0:
            res.append(path)
            return
        if left > 0:
            self.dfs(res, left-1, right, path + '(')
        if left < right:
            self.dfs(res, left, right-1, path + ')')


s = Solution()
res = s.generateParenthesis(3)
print(res)