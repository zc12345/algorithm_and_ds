#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File          :  merge_sort.py
@Time          :  2020/03/02 21:40:28
@Author        :  zc12345 
@Version       :  1.0
@Contact       :  2104158177@qq.com
@Description   :  None
'''

import random


def merge(left, right):
    sorted_arr = []
    while left and right:
        if left[0] < right[0]:
            sorted_arr.append(left.pop(0))
        else:
            sorted_arr.append(right.pop(0))
    if left:
        sorted_arr += left
    elif right:
        sorted_arr += right
    return sorted_arr


def merge_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        mid = len(arr) // 2
        left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
        sorted_arr = merge(left, right)
        return sorted_arr


if __name__ == "__main__":
    arr = [random.randint(0, 100) for i in range(10)]
    print(merge_sort(arr))
