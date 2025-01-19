#
# @lc app=leetcode id=525 lang=python3
#
# [525] Contiguous Array
#

# @lc code=start
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum = nums.copy()
        total = 0
        for i, num in enumerate(prefix_sum):
            total += prefix_sum[i]
            prefix_sum[i] = total


        max_length = 0
        for start, start_val in enumerate(prefix_sum):
            if start + max_length + 1 >= len(prefix_sum):
                break
            sub_array = prefix_sum[start + max_length + 1:]
            for end, end_val in enumerate(sub_array):
                if end + max_length + 2 == 2 * (end_val - start_val) :
                    max_length += (end + 2)

        return max_length



# @lc code=end

