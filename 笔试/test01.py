#!/usr/bin/env python
# encoding: utf-8
'''
@author: liuchang
@software: PyCharm
@file: test01.py
@time: 2020-07-31 15:16
'''
"""
输入：
1 1
输出：
2
"""
import sys
for line in sys.stdin:
    a = line.split()
    print(int(a[0]) + int(a[1]))