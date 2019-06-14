class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        n = len(candidates)
        res = []

        def helper(i, sum_temp, res_temp):
            if sum_temp == target:
                res.append(res_temp)
                return True
            for j in range(i, n):
                if sum_temp + candidates[j] > target:
                    break
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if helper(j + 1, sum_temp + candidates[j], res_temp + [candidates[j]]):
                    break

        helper(0, 0, [])
        return res


if __name__ == '__main__':
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    solution = Solution()
    print(solution.combinationSum2(candidates, target))
