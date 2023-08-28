#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        visited = [nums[0]]
        for i in nums:
            if i != visited[-1]:
                visited.append(i)

        # uniques = len(visited)
        # for i in range(len(nums)):
        #     if i < uniques:
        #         nums

        k = len(visited)
        # for i in range(len(nums) - k):
        #     visited.append('_')


        nums[:k] = visited

        return k


# @lc code=end

