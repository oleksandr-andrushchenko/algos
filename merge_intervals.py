# 🔹 4. Merge Intervals
import heapq


# 📌 Pattern Explanation:
# Used for solving problems related to merging overlapping intervals.

# 📌 Concept:
# Sort intervals by start time.
# Iterate and merge overlapping intervals.

# 📌 Popular Problems:
# Merge Overlapping Intervals
# Insert Interval
# Interval List Intersections
# Meeting Rooms
# Minimum Number of Platforms
# Employee Free Time

# 🔹 Merge Intervals Pattern

# 📌 Concept:
# The Merge Intervals pattern is used for solving problems that involve overlapping intervals.
#
# Common operations: Sorting, merging, inserting, or finding gaps between intervals.
# Sorting intervals by start time is the key first step in most problems.


# 🔹 Steps to Solve Merge Intervals Problems

# 1. Sort intervals based on the start time.
# 2. Iterate through intervals and compare end times:
# If intervals overlap → merge them.
# Otherwise → add them to the result.

# 1️⃣ Merge Overlapping Intervals
# 📌 Problem: Given a list of intervals, merge all overlapping intervals and return the merged intervals.

def merge_overlapping_intervals(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []

    # Sort intervals based on the start value
    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:
        # If merged is empty or the current interval doesn't overlap with the last merged interval
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # Merge the intervals by updating the end of the last merged interval
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


# Test Cases
assert merge_overlapping_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
assert merge_overlapping_intervals([[1, 4], [4, 5]]) == [[1, 5]]
assert merge_overlapping_intervals([[1, 4], [2, 3]]) == [[1, 4]]
assert merge_overlapping_intervals([[1, 5], [6, 8], [7, 9]]) == [[1, 5], [6, 9]]


# 2️⃣ Insert Interval
# 📌 Problem: Given a set of non-overlapping intervals sorted by start time and a new interval, insert the new interval into the list (merge if necessary).

def insert_interval(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    if not intervals:
        return [new_interval]

    inserted = False
    merged = []

    def merge(interval_to_add: list[int]):
        # If merged is empty or the current interval doesn't overlap with the last merged interval
        if not merged or merged[-1][1] < interval_to_add[0]:
            merged.append(interval_to_add)
        else:
            # Merge the intervals by updating the end of the last merged interval
            merged[-1][1] = max(merged[-1][1], interval_to_add[1])

    for i in range(len(intervals)):
        if new_interval[0] <= intervals[i][0]:
            merge(new_interval)
            inserted = True

        merge(intervals[i])

    if not inserted:
        merge(new_interval)

    return merged


# Test Cases
assert insert_interval([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
assert insert_interval([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [[1, 2], [3, 10], [12, 16]]
assert insert_interval([], [5, 7]) == [[5, 7]]
assert insert_interval([[1, 5]], [6, 8]) == [[1, 5], [6, 8]]


# 3️⃣ Interval List Intersections
# 📌 Problem: Given two lists of closed intervals, return their intersection.

# O(N + M)
def interval_intersection(first_list: list[list[int]], second_list: list[list[int]]) -> list[list[int]]:
    i, j = 0, 0
    result = []

    while i < len(first_list) and j < len(second_list):
        # Find the intersection between first_list[i] and second_list[j]
        start = max(first_list[i][0], second_list[j][0])  # Max of start times
        end = min(first_list[i][1], second_list[j][1])  # Min of end times

        if start <= end:  # Valid intersection
            result.append([start, end])

        # Move to the next interval in the list that finishes first
        if first_list[i][1] < second_list[j][1]:
            i += 1
        else:
            j += 1

    return result


# Test Cases
assert interval_intersection(
    [[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]]
) == [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
assert interval_intersection([[1, 3], [5, 9]], []) == []
assert interval_intersection([], [[4, 8], [10, 12]]) == []
assert interval_intersection([[1, 7]], [[3, 10]]) == [[3, 7]]


# 4️⃣ Meeting Rooms
# 📌 Problem: Given an array of meeting time intervals [start, end], determine if a person can attend all meetings.

# O(N log N) + O(N) = O(N log N)
def can_attend_meetings(intervals: list[list[int]]) -> bool:
    if not intervals:
        return True

    intervals.sort(key=lambda x: x[0])  # Sort by start time

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:  # Overlap detected
            return False  # Early exit

    return True


# Test Cases
assert can_attend_meetings([[0, 30], [5, 10], [15, 20]]) == False
assert can_attend_meetings([[7, 10], [2, 4]]) == True
assert can_attend_meetings([[1, 3], [3, 6], [7, 9]]) == True
assert can_attend_meetings([[1, 8], [2, 6], [9, 10]]) == False


# 5️⃣ Meeting Rooms II (Minimum Rooms Required)
# 📌 Problem: Given meeting time intervals [start, end], find the minimum number of conference rooms required.

# Sorting: O(N log N)
# Processing each interval: O(N log N) (heap operations)
# Total: O(N log N)
def min_meeting_rooms(intervals: list[list[int]]) -> int:
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[0])

    # Min-heap to track meeting end times
    # the number of active meetings at the end of the loop
    meeting_endings = []
    max_rooms = 0

    for start, end in intervals:
        while meeting_endings and meeting_endings[0] <= start:
            heapq.heappop(meeting_endings)

        heapq.heappush(meeting_endings, end)
        max_rooms = max(max_rooms, len(meeting_endings))

    return max_rooms


# Test Case
assert min_meeting_rooms([[0, 30], [5, 10], [15, 20]]) == 2
assert min_meeting_rooms([[7, 10], [2, 4]]) == 1
assert min_meeting_rooms([[1, 3], [2, 6], [5, 9]]) == 2
assert min_meeting_rooms([[1, 2], [2, 3], [3, 4]]) == 1


# 6️⃣ Employee Free Time
# 📌 Problem: Given the schedules of multiple employees, find all available free time slots.

# O(N log N)
def employee_free_time(schedule: list[list[list[int]]]) -> list[list[int]]:
    if not schedule:
        return []

    # Step 1: Flatten all intervals from different employees
    intervals = [interval for employee in schedule for interval in employee]

    # Step 2: Sort intervals by start time
    intervals.sort(key=lambda x: x[0])

    # Step 3: Merge overlapping intervals
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:  # No overlap
            merged.append(interval)
        else:  # Merge overlapping intervals
            merged[-1][1] = max(merged[-1][1], interval[1])

    # Step 4: Find gaps (free time) between merged intervals
    gaps = []
    for i in range(1, len(merged)):
        gaps.append([merged[i - 1][1], merged[i][0]])

    return gaps


# Test Cases
assert employee_free_time([[[1, 3], [6, 7]], [[2, 4]], [[2, 5], [9, 12]]]) == [[5, 6], [7, 9]]
assert employee_free_time([[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]) == [[3, 4]]
assert employee_free_time([[[1, 5]], [[10, 14]], [[19, 20], [21, 24]]]) == [[5, 10], [14, 19], [20, 21]]
assert employee_free_time([[[1, 5]], [[2, 6]], [[3, 7]]]) == []  # Fully overlapping meetings


# 7️⃣ Minimum Number of Platforms (Train Scheduling)
# 📌 Problem: Given arrival and departure times of trains, find the minimum number of platforms required.


def min_platforms(arrivals: list[int], departures: list[int]) -> int:
    max_platforms = 0

    intervals = [[arrivals[i], departures[i]] for i in range(len(arrivals))]
    intervals.sort(key=lambda x: x[0])

    # endings of intersected intervals for each round
    min_endings = []
    for start, end in intervals:

        if min_endings and start >= min_endings[0]:
            heapq.heappop(min_endings)

        heapq.heappush(min_endings, end)
        max_platforms = max(max_platforms, len(min_endings))

    return max_platforms


def min_platforms2(arrivals: list[int], departures: list[int]) -> int:
    intervals = [[arrivals[i], departures[i]] for i in range(len(arrivals))]

    return min_meeting_rooms(intervals)


# Test Cases
assert min_platforms([900, 940, 950, 1100, 1500, 1800], [910, 1200, 1120, 1130, 1900, 2000]) == 3
assert min_platforms([100, 200, 300, 400], [150, 250, 350, 450]) == 1
assert min_platforms([900, 915, 1030, 1115], [930, 1015, 1100, 1200]) == 2


# 8️⃣ Erase Overlapping Intervals
# 📌 Problem: Given an array of intervals, find the minimum number of intervals to remove so that the rest are non-overlapping.

# Sorting: O(N log N)
# Iterating through intervals: O(N)
# Total Complexity: O(N log N) (dominant sorting step)
def erase_overlap_intervals(intervals: list[list[int]]) -> int:
    if not intervals:
        return 0

    # Step 1: Sort intervals by end time
    intervals.sort(key=lambda x: x[1])

    # Step 2: Use greedy approach to track non-overlapping intervals
    removals = 0
    last_end = float('-inf')  # Start with a very small end time

    for start, end in intervals:
        if start < last_end:  # Overlapping interval found
            removals += 1  # Remove this interval
        else:
            last_end = end  # Update end time for next comparison

    return removals


# Test Cases
assert erase_overlap_intervals([[1, 2], [2, 3], [3, 4], [2, 6]]) == 1
assert erase_overlap_intervals([[1, 2], [1, 2], [1, 2]]) == 2
assert erase_overlap_intervals([[1, 2], [2, 3]]) == 0


# 9️⃣ Find Available Time Slots for Meetings
# 📌 Problem: Given booked meeting slots, return all available time slots for a new meeting of duration

def find_available_meeting_slots(intervals: list[list[int]], k: int) -> list[list[int]]:
    if not intervals:
        return [[0, k]]  # If no meetings, return the first available slot

    # Step 1: Sort intervals by start time
    intervals.sort(key=lambda x: x[0])

    # Step 2: Merge overlapping intervals
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:  # No overlap
            merged.append(interval)
        else:  # Merge overlapping intervals
            merged[-1][1] = max(merged[-1][1], interval[1])

    # Step 3: Find available slots
    free_slots = []

    # Check free time before the first meeting
    if merged[0][0] >= k:
        free_slots.append([0, merged[0][0]])

    # Check gaps between merged intervals
    for i in range(1, len(merged)):
        start = merged[i - 1][1]
        end = merged[i][0]
        if end - start >= k:
            free_slots.append([start, end])

    # ✅ Fix: Only add free slot after last meeting if it provides at least k duration
    last_end = merged[-1][1]
    if last_end + k >= last_end:  # Ensuring k duration is valid
        free_slots.append([last_end, last_end + k])

    return free_slots

# Re-running test cases
test_results = {
    "test_case_1": find_available_meeting_slots([[1, 3], [5, 6], [8, 9]], 2) == [[3, 5], [6, 8], [9, 11]],
    "test_case_2": find_available_meeting_slots([[1, 5], [5, 10]], 2) == [[10, 12]],
    "test_case_3": find_available_meeting_slots([], 1) == [[0, 1]],
    "test_case_4": find_available_meeting_slots([[1, 10]], 1) == [[10, 11]],  # Fixed!
    "test_case_5": find_available_meeting_slots([[2, 3], [4, 5], [6, 7]], 1) == [[0, 2], [3, 4], [5, 6], [7, 8]],
}

print(test_results)


