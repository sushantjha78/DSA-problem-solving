#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        largest_common_len = 0
        for start in range(len(text1)):
            text11 = text1[start:]
            common_len = 0
            prev = 0

            for i1 in range(len(text11)):
                for i2 in range(prev, len(text2)):
                    if text11[i1] == text2[i2]:
                        prev = i2 + 1
                        common_len += 1
                        break

        largest_common_len = max(largest_common_len, common_len)

        return largest_common_len


# @lc code=end
