#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # rules:
        # check if middle number of current array is less or more than the given no.
        # if the number is same then return the number
        # if the number is smaller than the given no. then
        # 1. perform the same process on the second half of the array

        middle = len(nums)//2
        if len(nums) <= 2 and target not in nums:
            return -1

        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            relative_idx =  self.search(nums[middle:], target)
            if relative_idx == -1:
                return -1
            else:
                return middle + relative_idx
        else:
            relative_idx = self.search(nums[:middle], target)
            if relative_idx == -1:
                return -1
            else:
                return relative_idx



# @lc code=end

