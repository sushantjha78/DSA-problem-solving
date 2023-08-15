#
# @lc app=leetcode id=1812 lang=python3
#
# [1812] Determine Color of a Chessboard Square
#

# @lc code=start
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        '''
        True : White
        False: Black
        '''

        color_row = (ord(coordinates[0]) - ord('a'))%2
        color_col = (int(coordinates[1]) - 1)%2

        if color_row == color_col:
            return False
        return True

# @lc code=end

