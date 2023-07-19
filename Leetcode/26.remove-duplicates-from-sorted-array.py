#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hashmap = {}
        uniques = 0
        for num in nums:
            if num not in hashmap:
                uniques += 1
                hashmap[num] = 1
            else:
                hashmap[num] += 1

        j = 0
        while j < len(nums):
            if hashmap[nums[j]] > 1:
                nums[j] = nums[j+]


# @lc code=end

