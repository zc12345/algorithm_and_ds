# python3
import sys


def main(inputs):
    sites = dict()
    for line in data:
        id_, site, period = line.split()
        if site not in sites:
            sites[site] = [[id_], int(period)]
        else:
            sites[site][0].append(id_)
            sites[site][1] += int(period)
    max_times, res = 0, None
    for site in sites:
        if sites[site][1] < 180:
            continue
        tmp = len(set(sites[site][0]))
        if tmp > max_times:
            res, max_times = site, tmp
    return res


if __name__ == "__main__":
    data = [
        "12678687 www.toutiao.com 31",
        "12678687 www.byte.com 60",
        "12678687 www.bytedance.com 210",
        "12678685 www.toutiao.com 20",
        "12678685 www.byte.com 90",
        "12678683 www.toutiao.com 15",
        "12678683 www.byte.com 40",
        "12678688 www.toutiao.com 15",
    ]
    # data = []
    # while True:
    #     line = sys.stdin.readline().strip()
    #     if not line:
    #         break
    #     data.append(line)
    res = main(data)
    print(res)
