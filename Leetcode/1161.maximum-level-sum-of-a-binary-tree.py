#
# @lc app=leetcode id=1161 lang=python3
#
# [1161] Maximum Level Sum of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # traverse the tree and store the nodes of each levelin a particular table
        # use a nested list as a table
        # traverse the list and find the max of the sum of the root values

        def traverse_append(node, level, table):
            if node != None:
                    try:
                        table[level].append(node.val)
                    except(IndexError):
                        table.append([])
                        table[level].append(node.val)

            if node.left != None:
                 traverse_append(node.left, level+1, table)

            if  node.right != None:
                 traverse_append(node.right, level+1, table)


        level = 0
        table = [[]]

        traverse_append(root, level, table)


        max_sum = -2**15
        max_sum_level = 0
        for i in range(len(table)):
            level_sum = sum(table[i])
            if level_sum > max_sum:
                max_sum = level_sum
                max_sum_level = i + 1

        return max_sum_level


# @lc code=end

