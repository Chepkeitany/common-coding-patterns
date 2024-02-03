'''
Given an array of meeting time intervals where intervals[i] = [starti, endi],
determine if a person could attend all meetings.
'''


def can_attend_all_meetings(intervals):
    # Sort the array by start time
    intervals.sort(key=lambda x: x[0])
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            # This meeting starts before the other one ends
            # The user cannot attend all meetings
            return False
    return True


if __name__ == "__main__":
    assert can_attend_all_meetings(
        [[0, 30], [5, 10], [15, 20]]) is False, "Failed on input [[0,30],[5,10],[15,20]]"
    assert can_attend_all_meetings(
        [[7, 10], [2, 4]]), "Failed on input [[7,10],[2,4]]"
    assert can_attend_all_meetings(
        [[1, 3], [2, 4]]) is False, "Failed on input [[1,3],[2,4]]"
    print("All tests passed!")
