'''
20.有效的括号
'''


class Solution:
    def isValid(self, s):
        array = list(s)
        dict = {'(': ')',
                '[': ']',
                '{': '}'}
        bracket_left = list('([{')
        stack = []
        while array:
            currentChar = array.pop(0)
            if bracket_left.count(currentChar) > 0:
                stack.extend([currentChar])
            else:
                if not stack:
                    return False
                else:
                    if dict[stack[-1]] == currentChar:
                        stack.pop()
                    else:
                        return False
        if not stack:
            return True
        else:
            return False
