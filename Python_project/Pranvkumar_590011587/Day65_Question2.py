def max_chain_length(pairs):
    # Sort by end value
    pairs.sort(key=lambda x: x[1])

    count = 0
    last_end = float('-inf')

    for a, b in pairs:
        if a > last_end:
            count += 1
            last_end = b
    return count

# Example
print(max_chain_length([(5, 24), (15, 25), (27, 40), (50, 60)]))  # Output: 3
print(max_chain_length([(1, 2), (2, 3), (3, 4)]))  # Output: 2
