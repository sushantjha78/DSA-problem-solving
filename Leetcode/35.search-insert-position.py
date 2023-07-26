#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        if len(nums) <= 2 and target not in nums:
            if len(nums) == 1:
                if nums[0] > target: return 0
                else: return 1

            elif len(nums) == 2:
                if nums[0] > target:
                    return 0
                elif nums[0] < target <= nums[1]:
                    return 1
                else: return 2

            else: return 0



        middle = len(nums)//2
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            relative_idx =  self.searchInsert(nums[middle:], target)
            middle + relative_idx
        else:
            relative_idx = self.searchInsert(nums[:middle], target)
            return relative_idx

# @lc code=end

