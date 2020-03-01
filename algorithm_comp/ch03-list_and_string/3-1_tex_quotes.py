#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File          :  3-1_tex_quotes.py
@Time          :  2020/01/29 14:26:42
@Author        :  zc12345 
@Version       :  1.0
@Contact       :  2104158177@qq.com
@Description   :  None
'''

def tex_quotes(s):
    '''UVa272 replace left quotes with tex quotes
    Time: 2020/01/29 22:31:35
    Args:
        s: {str} input string
    Returns:
        res: {str} output string
    '''
    flag = True
    res = []
    for ch in s:
        if ch == "\"":
            if flag:
                ch = "``"
            flag = not flag
        res.append(ch)
    return ''.join(res)

if __name__ == "__main__":
    s = "\"to be or not to be?\", he asked"
    s = tex_quotes(s)
    print(s)