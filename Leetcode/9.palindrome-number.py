#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 : return False
        if x < 10: return True

        else:
            digits=[]
            while x > 0:
                digits.append(x%10)
                x //= 10

        length_x = len(digits)
        for i in range(length_x//2):
            if digits[i] != digits[length_x-i-1]:
                return False

        return True


# @lc code=end

