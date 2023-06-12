# Your company built an in-house calendar tool called HiCal. You want to add a feature to see 
# the times in a day when everyone is available. In HiCal, a meeting is stored as a tuple of 
# integers (start_time, end_time). These integers represent the number of 30-minute blocks 
# past 9:00am.  Write a function merge_ranges() that takes a list of multiple meeting time 
# ranges and returns a list of condensed ranges.
# For example, given: [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)] your function would return:
# [(0, 1), (3, 8), (9, 12)].

def merge_ranges(meetings):
# to merge to time ranges we consider that the end time of the first meeting and the start time
# of the second meeting are equal, or the second meeting ends before the first meeting ends.
# 1. We treat the meeting with earlier start time as "first," and the other as "second."
# If the end time of the first meeting is equal to or greater than the start time of the second
# meeting, we merge the two meetings into one time range. The resulting time range's start time
# is the first meeting's start, and its end time is the later of the two meetings' end times.
# Else, we leave them separate.  In order to solve this problem in a time less than O(n2), we
# use a greedy approach, where the last meeting add to the merged list is considered the first 
# meeting to merge(or not) and the merged list is altered accordingly at each step of the loop
    sort_meets = sorted(meetings)  # this is to have the list of meetings in chronological order
    output = [sort_meets[0]] #merged list is initialized with the first meet of the day
    for current_meet in sort_meets[1:]: # the meetings are traverse starting from the second meet
        if current_meet[0]<= output[-1][1]: #-1 index means the last entry of the list
            output[-1]= (output[-1][0],max([current_meet[1],output[-1][1]]))
        else:
            output.append(current_meet)
    return output

list_meets = [(0,1),(3,5),(4,8),(10,12),(9,10)]
output = merge_ranges(list_meets)
print(len(list_meets))
print(output)