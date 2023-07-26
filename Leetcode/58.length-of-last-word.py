#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        for c in s[::-1]:
            if c != ' ':
                length += 1

            elif c == ' ' and length == 0:
                pass

            else: return length

        return length


# @lc code=end

