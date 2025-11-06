from typing import List, Tuple

def fractional_knapsack(weights: List[float], values: List[float], capacity: float
                       ) -> Tuple[float, List[Tuple[int, float]]]:
    n = len(weights)
    if n != len(values):
        raise ValueError("weights and values must be same length")
    if capacity <= 0:
        return 0.0, []

    items = [
        (i, values[i], weights[i], (values[i] / weights[i]) if weights[i] > 0 else float('inf'))
        for i in range(n)
    ]
    # sort by value/weight ratio descending
    items.sort(key=lambda x: x[3], reverse=True)

    total_value = 0.0
    taken: List[Tuple[int, float]] = []
    remaining = capacity

    for idx, val, wt, ratio in items:
        if remaining <= 0:
            break
        if wt <= remaining:
            total_value += val
            taken.append((idx, 1.0))
            remaining -= wt
        else:
            frac = remaining / wt
            total_value += val * frac
            taken.append((idx, frac))
            remaining = 0
            break

    return total_value, taken


def knapsack_01_dp(weights: List[int], values: List[int], capacity: int
                  ) -> Tuple[int, List[int]]:
    n = len(weights)
    if n != len(values):
        raise ValueError("weights and values must be same length")
    if capacity <= 0 or n == 0:
        return 0, []

    # dp[w] = max value for capacity w; use 1D optimized DP and track choices separately
    dp = [0] * (capacity + 1)
    # keep track of item choice at each stage: prev_choice[i][w] = True if item i used for capacity w
    # To reconstruct choices we store parent pointers: parent[i][w] = previous capacity before taking item i
    parent = [[-1] * (capacity + 1) for _ in range(n)]

    for i in range(n):
        wt = weights[i]
        val = values[i]
        # iterate capacities descending to avoid reuse
        for w in range(capacity, wt - 1, -1):
            new_val = dp[w - wt] + val
            if new_val > dp[w]:
                dp[w] = new_val
                parent[i][w] = w - wt  # record that at item i and capacity w we came from w-wt

    # reconstruct selected items by scanning from last item backwards
    w = capacity
    selected = []
    for i in range(n - 1, -1, -1):
        if parent[i][w] != -1:
            selected.append(i)
            w = parent[i][w]
            if w == 0:
                break

    selected.reverse()
    return dp[capacity], selected


if __name__ == "__main__":
    # Example usage
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50

    print("Fractional Knapsack (Greedy):")
    val_frac, items_frac = fractional_knapsack(weights, values, capacity)
    print(f"  Max value: {val_frac}")
    print(f"  Taken (index, fraction): {items_frac}")

    print("\n0/1 Knapsack (Dynamic Programming):")
    val01, items01 = knapsack_01_dp(weights, values, capacity)
    print(f"  Max value: {val01}")
    print(f"  Taken indices: {items01}")