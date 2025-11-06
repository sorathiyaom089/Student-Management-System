from typing import List, Tuple


def activity_selection(activities: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    # sort by finish time
    sorted_acts = sorted(activities, key=lambda x: x[1])
    selected: List[Tuple[int, int]] = []
    last_finish = -float("inf")

    for start, finish in sorted_acts:
        if start >= last_finish:
            selected.append((start, finish))
            last_finish = finish

    return selected

if __name__ == "__main__":
    activities = [(1, 3), (2, 5), (4, 6), (6, 7), (5, 9), (8, 9)]
    chosen = activity_selection(activities)
    print("Selected activities (start, finish):", chosen)
    print("Count:", len(chosen))