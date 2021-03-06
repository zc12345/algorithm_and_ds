#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File          :  binary_search.py
@Time          :  2020/02/02 15:30:17
@Author        :  zc12345 
@Version       :  1.0
@Contact       :  2104158177@qq.com
@Description   :  binary search
'''

def search(arr, element):
    '''info
    Time: 2020/02/02 15:31:19
    Args:
        arr: {int} input array
        element: {int} search element
    Returns:
        None
    '''
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < element:
            low = mid + 1
        elif arr[mid] > element:
            high = mid - 1
        else:
            return mid
    return None

if __name__ == "__main__":
    arr = [1, 2, 4]
    e = 4
    i = search(arr, e)
    print(i)
