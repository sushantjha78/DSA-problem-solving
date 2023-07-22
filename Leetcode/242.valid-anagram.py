#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # to get the occurance of each alphabet in a word
        def create_hash(word: str) -> dict:
            alphabets = {}
            for alphabet in word:
                if alphabet in alphabets:
                    alphabets[alphabet] += 1
                else:
                    alphabets[alphabet] = 1
            return alphabets

        hash_s = create_hash(s)
        hash_t = create_hash(t)

        for key in hash_s:
            if key not in hash_t:
                return False
            elif hash_s[key] != hash_t[key]:
                return False

        for key in hash_t:
            if key not in hash_s:
                return False
            elif hash_t[key] != hash_s[key]:
                return False

        return True


# @lc code=end

