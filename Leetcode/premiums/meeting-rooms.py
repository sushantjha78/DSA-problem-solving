# rediscovered bubble sort



"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # bruteforce sort
        # [9,1,6,3,8]
        num_meetings = len(intervals)
        if num_meetings  < 2: return True

        for i in range(num_meetings):
            smallest = intervals[i].start
            curr_idx = i
            for j in range(i, num_meetings):
                if intervals[j].start < smallest:
                    smallest = intervals[j].start
                    curr_idx = j

            intervals[i], intervals[curr_idx] = intervals[curr_idx], intervals[i]

        for i in range(num_meetings -1):
            if intervals[i].end > intervals[i+1].start :
                return False

        return True