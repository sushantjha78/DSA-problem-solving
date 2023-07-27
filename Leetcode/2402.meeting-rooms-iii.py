#
# @lc app=leetcode id=2402 lang=python3
#
# [2402] Meeting Rooms III
#

# @lc code=start
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # keep count of number of meetings in each room
        # keep track of busy rooms
        # keep a queue for the meetings and dequeue when a room available
        # perform unti queue is empty

        meet_counts = [0 for rooms in range(n)]
        busy = [False for rooms in range(n)]

        while len(meetings) > 0:
            for room in range(n):
                pass



# @lc code=end

