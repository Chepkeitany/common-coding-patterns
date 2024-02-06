'''
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi],
return the minimum number of conference rooms required.
'''

import heapq


def minimum_meeting_rooms(intervals):
    """Find the minimum rooms required for all meetings"""
    if not intervals:
        return 0
    # Sort meetings by start time
    intervals.sort(key=lambda x: x[0])

    min_rooms = 0
    minimum_rooms_heap = []

    for interval in intervals:
        while minimum_rooms_heap and interval[0] >= minimum_rooms_heap[0]:
            heapq.heappop(minimum_rooms_heap)

        heapq.heappush(minimum_rooms_heap, interval[1])

        min_rooms = max(min_rooms, len(minimum_rooms_heap))

    return min_rooms


if __name__ == "__main__":
    assert minimum_meeting_rooms(
        [[0, 30], [5, 10], [15, 20]]) == 2, "Failed on input [[0,30],[5,10],[15,20]]"
    assert minimum_meeting_rooms(
        [[7, 10], [2, 4]]) == 1, "Failed on input [[7,10],[2,4]]"

    print("All tests passed!")
