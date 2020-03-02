#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File          :  select_sort.py
@Time          :  2020/03/02 17:50:58
@Author        :  zc12345 
@Version       :  1.0
@Contact       :  2104158177@qq.com
@Description   :  None
'''

def find_samllest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def select_sort(arr):
    sorted_arr = []
    for i in range(len(arr)):
        smallest_index = find_samllest(arr)
        sorted_arr.append(arr.pop(smallest_index))
    return sorted_arr

if __name__ == "__main__":
    arr = [1, 2, 8, 3, 5, 0, 12, 7]
    print(select_sort(arr))
