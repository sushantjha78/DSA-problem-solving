#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ")" :"(",
            "}" : '{',
            "]" : "[",
        }

        # solution of O(n)
        for bracket in s:
            if bracket in pairs.keys() and pairs[bracket] in stack:
                if stack[-1] == pairs[bracket]:
                    stack.pop()
            else:
                stack.append(bracket)

        if len(stack) == 0:
            return True
        else: return False




# @lc code=end

