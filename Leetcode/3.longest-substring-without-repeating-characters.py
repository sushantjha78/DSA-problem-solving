#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tally = [0 for i in range(128)]
        max_len = 0
        curr_len = 0
        start = 0
        for i in range(len(s)):
            if tally[ord(s[i])] == 0:
                tally[ord(s[i])] += 1
                curr_len += 1
                max_len = max(curr_len, max_len)
            else:
                for j in range(start, i):
                    if ord(s[j]) == ord(s[i]):
                        curr_len = i-j
                        start = j+1
                        break
                    else:
                        tally[ord(s[j])] = 0

        return max_len



# @lc code=end

