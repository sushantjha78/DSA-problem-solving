#
# @lc app=leetcode id=263 lang=python3
#
# [263] Ugly Number
#

# @lc code=start
class Solution:
    def isUgly(self, n: int) -> bool:
        # its ugly if 2,3,5 are the only prime factors
        # 7*11 = 77 as a factor then false

        ugly_factors = [2, 3, 5]
        was_divisible = False
        other_factors = False

        for factor in ugly_factors:
            while n % factor == 0:
                n //= factor
                was_divisible = True

        # for i in range(2, n+1):
        #     if n % i == 0:
        #         return False

        if n not in (1, 0,-1) :
            return False

        return True

# @lc code=end

