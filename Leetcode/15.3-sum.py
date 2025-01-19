#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hashmap = {}
        output = set()

        for i, num in enumerate(nums):
            if num not in hashmap:
                hashmap[num] = [i]
            else:
                hashmap[num].append(i)

        # so now we have a map of numbers and  their indices
        # O(1) search

        for i, num1 in enumerate(nums[:-2]):
            for j, num2 in enumerate(nums[i+1:-1]):
                num3 = 0 - num1 - num2
                if (num3 in hashmap):
                    for idx in hashmap[num3]:
                        if idx > i + j + 1:
                            output.add(tuple(sorted([num1, num2, num3])))

        final_output = []
        for tuples in output:
            final_output.append(list(tuples))


        return final_output




# @lc code=end

