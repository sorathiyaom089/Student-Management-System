def min_removals(intervals):
    intervals.sort(key=lambda x: x[1])  # sort by end time
    count = 0
    last_end = float('-inf')

    for start, end in intervals:
        if start >= last_end:  # valid, non-overlapping
            count += 1
            last_end = end
    return len(intervals) - count  # tasks removed = total - kept

# Example
print("Remove", min_removals([(1, 2), (2, 3), (3, 4), (1, 3)]))  # Output: Remove 1
print("Remove", min_removals([(1, 2), (1, 2), (1, 2)]))          # Output: Remove 2
