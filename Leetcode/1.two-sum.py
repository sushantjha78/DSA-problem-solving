#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ### Brute force

        # lenArray = len(nums)
        # for i in range(lenArray):
        #     for j in range(i+1, lenArray):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        # sort - O(n log n)
        # iterate over elements and search for other element
        #      - O(n * log n)

        #  so total - O(2 n log n)


        #### hash table O(n)
        numDict = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in numDict:
                return [i, numDict[compliment]]
            numDict[nums[i]] = i

        return []

# @lc code=end

