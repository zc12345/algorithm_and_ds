'''
2020/03/18
华为笔试题3
打怪兽问题（未解决）
已知n行m列的矩阵，其中0是陷阱，不能通过，1可以通过，2-n表示不同级别的怪兽，奥特曼要按照从低到高的顺序打败怪兽才能通行
问能否消灭所有怪兽？如果能，返回最少步数，不能则返回-1
'''

def search(m, n):
    return -1
    i, j = 1, 1
    step = 0
    sums = 0
    t = [[0 for ii in range(n+2)] for jj in range(n+2)] # padding 0
    for p in range(n):
        for q in range(n):
            t[p+1][q+1] = m[p][q]
            sums += m[p][q]
    while i<n+1 and j<n+1:
        if t[i-1][j]==0 and t[j][j-1]==0 and t[i+1][j]==0 and t[i][j+1]==0 and sums > 0:
            return -1
        if sums == 0:
            return step
        neighbors = [[i-1,j], [i,j-1], [i+1,j], [i,j+1]]
        for index in neighbors:
            tmp = t[index[0]][index[1]]
            if tmp == t[i][j] + 1:
                sums -= tmp
                i, j = index
    return -1

if __name__ == "__main__":
    m = [[1, 2, 0],[0, 3, 4],[0, 6, 5]]
    n = len(m)
    ans = search(m, n)
    print(ans)