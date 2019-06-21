'''
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
'''


class Solution:
    def generateParenthesis(self, n):
        res = []

        def helper(charTemp, nLeft, nRight):
            if nLeft < n:
                helper(charTemp + '(', nLeft + 1, nRight)
            if nLeft > nRight and nRight < n:
                helper(charTemp + ')', nLeft, nRight + 1)
            if nLeft == n and nRight == n:
                res.append(charTemp)

        helper('', 0, 0)
        return res
