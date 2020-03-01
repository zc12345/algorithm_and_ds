#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File          :  3-2_WERTYU.py
@Time          :  2020/01/29 22:43:47
@Author        :  zc12345 
@Version       :  1.0
@Contact       :  2104158177@qq.com
@Description   :  None
'''

def WERTYU(s):
    s1 = '`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;\'ZXCVBNM,./'
    res = []
    for ch in s:
        for i in range(len(s1)):
            if ch == s1[i]:
                ch = s1[i-1]
                break
        res.append(ch)
    return ''.join(res)

if __name__ == "__main__":
    s = "O S, GOMR YPFSU"
    r = WERTYU(s)
    print(r)