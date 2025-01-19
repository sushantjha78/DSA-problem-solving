#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums


    def sumRange(self, left: int, right: int) -> int:
        total = 0
        prefix_sum = self.nums.copy()
        for idx, num in enumerate(prefix_sum):
            total += num
            prefix_sum[idx] = total

        if left == 0:
            return prefix_sum[right]

        return prefix_sum[right] - prefix_sum[left-1]




# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end

