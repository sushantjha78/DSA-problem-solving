#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_string = ''.join(char for char in s if 'a' <= char <= 'z' or '0' <= char <= '9')

        length = len(new_string)
        for i, char in enumerate(new_string):
            if new_string[length-i-1] != char:
                return False

        return True



# @lc code=end

