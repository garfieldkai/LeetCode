class Solution:
    '''
    给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
    https://leetcode-cn.com/problems/combination-sum/
    '''
    def combinationSum(self, candidates, target):
        candidates.sort()
        n = len(candidates)
        res = []
        def backtrack(i, tmp_sum, tmp):
            # if  tmp_sum > target or i == n:
            #     return
            if tmp_sum == target:
                res.append(tmp)
                return True
            for j in range(i, n):
                if tmp_sum + candidates[j] > target:
                    break
                if backtrack(j,tmp_sum + candidates[j],tmp+[candidates[j]]):
                    break
        backtrack(0, 0, [])
        return res
if __name__ == '__main__':
    candidates = [2,3,6,7]
    target = 7
    solution = Solution()
    print(solution.combinationSum(candidates,target))