
class Solution1:
    def paradox(self, K, N, values):
        back = 0
        if K == 0:
            if N > 0:
                return 'paradox'
            else:
                return [0, 0]
        for i in range(N):
            K -= values[i]
            if K == 0:
                if i < N-1:
                    return 'paradox'
                else:
                    break
            elif K > 0:
                continue
            else:
                K = abs(K)
                back += 1
        return [abs(K), back]


class Solution2:
    def isSame(self, nums):
        d = {}
        for values in nums:
            temp = self.rotate(values)
            temp = [str(i) for i in temp]
            temp = ''.join(temp)
            if temp in d:
                d[temp] += 1
            else:
                d[temp] = 1
        # d = sorted(d.items(), key=lambda a:a[1], reverse=True)
        res = []
        for key in d:
            res.append(d[key])
        return res

    def rotate(self, nums):
        ans = []
        idx = 0
        ans.append(1)
        for i in range(6):
            if nums[i] == 1:
                idx = i
                break
        if idx == 0:
            ans.append(nums[1])
            next_min = min(nums[2:])
            ans.append(next_min)
            idx1 = 2
            for j in range(2, 6):
                if nums[j] == next_min:
                    idx1 = j
                    break
            d = {
                2: [4, 3, 5],
                3: [5, 2, 4],
                4: [3, 5, 2],
                5: [2, 4, 3],
                1: [2, 4, 3],
            }
            for t_i in d[idx1]:
                ans.append(nums[t_i])
        elif idx == 1:
            ans.append(nums[0])
            next_min = min(nums[2:])
            ans.append(next_min)
            idx1 = 2
            for j in range(2, 6):
                if nums[j] == next_min:
                    idx1 = j
                    break
            d = {
                2: [5, 3, 4],
                3: [4, 2, 5],
                4: [2, 5, 3],
                5: [3, 4, 2],
                0: [2, 4, 3],
            }
            for t_i in d[idx1]:
                ans.append(nums[t_i])
        elif idx == 2:
            ans.append(nums[3])
            next_min = min(nums[0], nums[1], nums[4], nums[5])
            ans.append(next_min)
            idx1 = 2
            for j in range(2, 6):
                if nums[j] == next_min:
                    idx1 = j
                    break
            d = {
                0: [5, 1, 4],
                1: [4, 0, 5],
                4: [0, 5, 1],
                5: [1, 4, 0],
                3: [1, 4, 0],
            }
            for t_i in d[idx1]:
                ans.append(nums[t_i])
        elif idx == 3:
            ans.append(nums[2])
            next_min = min(nums[0], nums[1], nums[4], nums[5])
            ans.append(next_min)
            idx1 = 0
            for j in range(0, 6):
                if nums[j] == next_min:
                    idx1 = j
                    break
            d = {
                0: [4, 1, 5],
                1: [5, 0, 4],
                4: [1, 5, 0],
                5: [0, 4, 1],
                2: [0, 4, 1],
            }
            for t_i in d[idx1]:
                ans.append(nums[t_i])
        elif idx == 4:
            ans.append(nums[5])
            next_min = min(nums[:4])
            ans.append(next_min)
            idx1 = 0
            for j in range(0, 6):
                if nums[j] == next_min:
                    idx1 = j
                    break
            d = {
                0: [2, 1, 3],
                1: [3, 0, 2],
                2: [1, 3, 0],
                5: [0, 2, 1],
                3: [0, 2, 1],
            }
            for t_i in d[idx1]:
                ans.append(nums[t_i])
        else:
            ans.append(nums[4])
            next_min = min(nums[:4])
            ans.append(next_min)
            idx1 = 0
            for j in range(0, 6):
                if nums[j] == next_min:
                    idx1 = j
                    break
            d = {
                0: [3, 1, 2],
                1: [2, 0, 3],
                2: [0, 3, 1],
                3: [1, 2, 0],
                4: [1, 2, 0],
                5: [1, 2, 0],
            }
            for t_i in d[idx1]:
                ans.append(nums[t_i])
        return ans


class Solution3:
    def maxValue(self, N, M, T, food_noon, food_night):
        res = float('inf')
        food_noon.append([0, 0])
        food_night.append([0, 0])
        N, M = N+1, M+1
        food_noon.sort(key=lambda x: x[1])
        food_night.sort(key=lambda x: x[1])
        temp = [0]*M
        tmp = float('inf')
        for i in range(M-1, -1, -1):
            tmp = min(food_night[i][0], tmp)
            temp[i] = tmp
        for i in range(N):
            tmp = T-food_noon[i][1]
            if tmp <= 0:
                res = min(res, food_noon[i][0])
                continue
            left, right = 0, M-1
            while left < right:
                mid = (left+right) // 2
                if tmp == food_night[mid][1]:
                    left = mid
                    break
                elif tmp > food_night[mid][1]:
                    left = mid + 1
                else:
                    right = mid
            if food_night[left][1] >= tmp:
                res = min(res, food_noon[i][0]+temp[left])
        return res if res != float('inf') else -1


class Solution4:
    def maxPlans(self, s):
        pass


if __name__ == "__main__":
    ############
    #problem 01#
    ############
    # K, N, values = 10, 2, [6, 3]
    # K, N, values = 10, 4, [6, 3, 3, 3]
    # K, N, values = 0, 3, [4, 2, 6]
    # res = Solution().paradox(K, N, values)
    # if res == 'paradox':
    #     print(res)
    # else:
    #     print(res[0], res[1])

    ############
    #problem 02#
    ############
    values = [
        [1, 2, 3, 4, 5, 6],
        [1, 2, 6, 5, 3, 4]
    ]
    res = Solution2().isSame(values)
    res = sorted(res, reverse=True)
    print(len(res))
    s = ' '.join([str(i) for i in res])
    print(s)

    ############
    #problem 03#
    ############
    # N, M, T = 5, 1, 9
    # food_noon = [
    #     [9, 1],
    #     [4, 9],
    #     [3, 1],
    #     [2, 3],
    #     [6, 5]
    # ]
    # food_night = [
    #     [9, 8]
    # ]
    # res = Solution3().maxValue(N, M, T, food_noon, food_night)
    # print(res)

    ############
    #problem 04#
    ############
    # s = [
    #     '#*****',
    #     '******',
    #     '******',
    #     '******',
    #     '******',
    #     '*****#'
    # ]
    # res = Solution4().maxPlans(s)
    # print(res)
