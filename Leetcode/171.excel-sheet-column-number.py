#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        output = 0
        for c in columnTitle:
            output *= 26
            output += (ord(c) - ord('A') + 1)

        return output

# @lc code=end

