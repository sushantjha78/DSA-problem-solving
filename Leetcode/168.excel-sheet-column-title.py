#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        output = ""
        while columnNumber:
            output += chr(ord('A') + (columnNumber-1)%26)
            columnNumber = (columnNumber-1)//26

        return output[::-1]


# @lc code=end

