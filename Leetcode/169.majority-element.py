#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1

            else: count[num] += 1

        max_count = 0
        max_val = 0
        for num in count.keys():
            if count[num] > max_count:
                max_count = count[num]
                max_val = num

        return max_val


# @lc code=end

