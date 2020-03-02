#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File          :  quick_sort.py
@Time          :  2020/03/02 20:55:10
@Author        :  zc12345 
@Version       :  1.0
@Contact       :  2104158177@qq.com
@Description   :  None
'''

import random


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        arr.pop(0)
        less = [i for i in arr if i <= pivot]
        greater = [i for i in arr if i > pivot]  # 遍历数组，时间为O(n)
        return quick_sort(less) + [pivot] + quick_sort(greater)


def quick_sort2(arr, left, right):
    if left < right:
        index = partition1(arr, left, right)
        quick_sort2(arr, left, index - 1)
        quick_sort2(arr, index + 1, right)
    return arr


def partition1(arr, left, right):
    x = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


def partition2(arr, left, right):
    tmp = arr[left]
    i = left
    j = right  # 从两头交替进行遍历，时间减半，1/2 O(n)
    while i < j:  # i == j时跳出循环
        while i < j and arr[j] >= tmp:
            j -= 1
        arr[i] = arr[j]  # 如果队尾元素小于基准值，将其赋值给左侧
        while i < j and arr[i] < tmp:
            i += 1
        arr[j] = arr[i]  # 如果队尾元素大于基准值，将其赋值给右侧
    arr[i] = tmp
    return i


if __name__ == "__main__":
    arr = [random.randint(0, 100) for i in range(10000)]
    arr = quick_sort2(arr, 0, len(arr) - 1)
    print(arr)

    # ts1 = []
    # ts2 = []
    # for i in range(100):
    #     arr = [random.randint(0, 100) for i in range(10000)]
    #     import time
    #     t0 = time.time()
    #     arr = quick_sort2(arr, 0, len(arr)-1)
    #     t1 = time.time()
    #     t = t1-t0
    #     ts1.append(t)
    #     t0 = time.time()
    #     arr = quick_sort(arr)
    #     t1 = time.time()
    #     t = t1-t0
    #     ts2.append(t)
    # print(sum(ts1), sum(ts2))
