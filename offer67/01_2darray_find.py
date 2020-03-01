'''
题目描述
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''
# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        col, row = len(array), len(array[0])
        for i in range(col):
            low, high = 0, row - 1
            while low <= high:
                mid = (low + high) // 2
                if target > array[i][mid]:
                    low = mid + 1
                elif target < array[i][mid]:
                    high = mid - 1
                else:
                    return True
        return False

if __name__ == "__main__":
    target = 3
    array = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    res = Solution().Find(target, array)
    print(res)