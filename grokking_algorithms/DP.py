#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File          :  DP.py
@Time          :  2020/03/06 21:41:39
@Author        :  zc12345 
@Version       :  1.0
@Contact       :  2104158177@qq.com
@Description   :  Dynamic Programming
'''


def longest_common_substring(str1, str2):
    m = [[0 for i in range(len(str2)+1)] for j in range(len(str1)+1)]
    m_max = 0
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                m[i+1][j+1] = m[i][j]+1
                m_max = max(m_max, m[i+1][j+1])
    return m_max


def longest_common_subchars(str1, str2):
    m = [[0 for i in range(len(str2)+1)] for j in range(len(str1)+1)]
    m_max = 0
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                m[i+1][j+1] = m[i][j]+1
            else:
                m[i+1][j+1] = max(m[i+1][j], m[i][j+1])
            m_max = max(m_max, m[i+1][j+1])
    return m_max


if __name__ == "__main__":
    s1 = 'fish'
    s2 = 'histh'
    res1 = longest_common_substring(s1, s2)
    res2 = longest_common_subchars(s1, s2)
    print(res1, res2)
