'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
'''


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapDict = {'2': list('abc'),
                   '3': list('def'),
                   '4': list('ghi'),
                   '5': ['j', 'k', 'l'],
                   '6': ['m', 'n', 'o'],
                   '7': ['p', 'q', 'r', 's'],
                   '8': ['t', 'u', 'v'],
                   '9': ['w', 'x', 'y', 'z']}
        res = []

        def helper(coordinate, digits_temp):
            if not digits_temp:
                res.append(coordinate)
            else:
                for digit in mapDict[digits_temp[0]]:
                    helper(coordinate + digit, digits_temp[1:])

        if digits:
            helper("", list(digits))
        return res
