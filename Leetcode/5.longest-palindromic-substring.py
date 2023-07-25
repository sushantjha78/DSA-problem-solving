#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        indices = [0,0]
        max_palindrome = 0

        def is_palindrome(word):
            for i in range(len(word)//2):
                if word[i] != word[len(word) - i -1]:
                    return False
            return True


        for start in range(len(s)):
            for end in range(start + max_palindrome + 1, len(s)+1):
                if is_palindrome(s[start:end]):
                    max_palindrome = end - start
                    indices = [start, end]


        if len(s) <= 1:
            return s

        else: return s[indices[0]:indices[1]]


# @lc code=end

