#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_meaning = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000,
        }

        alternate_roman_meaning = {
        'V':-1,
        'X':-1,
        'L':-10,
        'C':-10,
        'D':-100,
        'M':-100,
        }

        final_num = 0
        for idx in range(len(s)):
            if idx<len(s)-1 and roman_meaning[s[idx]] < roman_meaning[s[idx+1]]:
                final_num -= roman_meaning[s[idx]]
            else:
                final_num += roman_meaning[s[idx]]

        return final_num

# @lc code=end

