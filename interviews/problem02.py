'''
2020/03/18
华为笔试题1
IP1，IP2，mask分别为两个IP地址和子网掩码
求两个IP是否位于同一个网关（IP和子网掩码的按位与结果相等），并输出IP1的网关地址
'''


def check(ip1, ip2, mask):
    res0, res1, res2 = 1, [], []
    ips1, ips2, masks = ip1.split('.'), ip2.split('.'), mask.split('.')
    print(ips1, ips2, masks)
    for i in range(len(ips1)):
        a = int(ips1[i]) & int(masks[i])
        b = int(ips2[i]) & int(masks[i])
        print(a, b)
        if not a==b:
            res0 = 0
        res1.append(a)
    res = '{}.{}.{}.{}'.format(res1[0], res1[1], res1[2], res1[3])
    return res0, res

if __name__ == "__main__":
    ip1 = '192.168.1.1'
    ip2 = '192.168.2.1'
    mask = '255.255.255.0'
    res1, res2 = check(ip1, ip2, mask)
    print(res1, res2)