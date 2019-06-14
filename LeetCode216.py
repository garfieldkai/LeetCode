class Solution:
    '''
    找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
    说明：
    所有数字都是正整数。
    解集不能包含重复的组合。
    '''

    def combinationSum3(self, k, n):
        nums = range(1, 10)
        res = []

        def helper(i, sum_temp, res_temp):
            if sum_temp == n and len(res_temp) == k:
                res.append(res_temp)
                return
            for j in range(i, 9):
                print(j)
                if sum_temp + nums[j] > n:
                    break
                if len(res_temp) > k:
                    break
                if helper(j + 1, sum_temp + nums[j], res_temp + [nums[j]]):
                    break

        helper(0, 0, [])
        return res


if __name__ == '__main__':
    k = 3
    n = 9
    solution = Solution()
    print(solution.combinationSum3(k, n))
