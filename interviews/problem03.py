'''
2020/03/18
华为笔试题2(Leetcode 221 最大正方形)
n为矩阵行数，已知m*n大小的矩阵，求最大的全1正方形子矩阵
'''

def search_matrix(m, n):
    if n<2:
        return n
    h, w = len(m), len(m[0])
    res = 0
    p = [[0 for ii in range(w+1)] for jj in range(h+1)]
    for i in range(1, h+1):
        for j in range(1, w+1):
            if m[i-1][j-1] == 1:
                p[i][j] = min(p[i-1][j-1], p[i][j-1], p[i-1][j]) + 1
                res = max(res, p[i][j])
    return res*res

if __name__ == "__main__":
    # 读取第一行的n
    n = 3
    ans = [[1,1,0],[1,1,1],[1,1,0]]
    res = search_matrix(ans, n)
    print(res)