#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        search_size = len(needle)

        for idx in range(len(haystack) - search_size +1):
            if haystack[idx:idx+search_size] == needle:
                return idx

        if needle == haystack:
            return 0

        return -1

# @lc code=end

