#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = strs[0]
        for word in strs[1:]:
            if word == "":
                common_prefix = ""
                common_len = 0
                break

            for i in range(len(word)):
                common_len = 0
                while (i + common_len) < len(common_prefix) and (i + common_len) < len(word) and common_prefix[i + common_len] == word[i + common_len]:
                    common_len += 1

                common_prefix = word[i: i + common_len]
                break
        return common_prefix




    ### BELOW CODE IS FOR LONGEST COMMON SUBSTRING ###
    #     def find_common(word1, word2):
    #         common_len = 0
    #         common_str = ""
    #         for i1 in range(len(word1)):
    #             for i2 in range(len(word2)):
    #                 offset = 0
    #                 while (i1 + offset) < len(word1) and (i2 + offset) < len(word2) and word1[i1 + offset] == word2[i2 + offset]:
    #                     offset += 1


    #                 if offset > common_len:
    #                     common_len = offset
    #                     common_str = word1[i1 : i1 + offset]
    #         return common_str



    #     common_word = strs[0]
    #     for curr_word in strs[1:]:
    #         common_word = find_common(common_word, curr_word)
    #         if common_word == "":
    #             break

    #     return common_word




# @lc code=end

