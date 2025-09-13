# Day 65 (19/08/2025/) 
# 1. Minimum Coins 
# A problem that demonstrates currency optimization and teaches greedy coin selection 
# algorithms using denomination-based approach for efficient change-making and cost 
# minimization operations. 
# Given coins of different denominations, find the minimum number of coins to make a 
# given amount using greedy selection strategy. This operation is fundamental in currency 
# exchange and change optimization where you need to minimize transaction complexity 
# while achieving target amounts efficiently. The technique uses largest denomination first 
# greedy approach to always select the highest value coin possible, reducing the total number 
# of coins needed. This concept is essential in payment systems, cash register operations, and 
# financial transactions where minimizing coin count enables efficient currency handling and 
# optimal transaction processing in monetary exchange scenarios. 
# This demonstrates coin optimization algorithms and denomination selection techniques 
# that are crucial for currency management and efficient change-making operations. 
# Your task: Implement greedy coin selection using largest denomination strategy to minimize 
# coin count while achieving exact amount targets with optimal efficiency. 
# Examples 
# Input: 
# coins = [1, 2, 5, 10], amount = 23 
# Output: 
# 5 (10+10+2+1) 
# Input: 
# coins = [1, 5, 6, 9], amount = 11 
# Output: 
# 2 (5+6) 
# 2. Maximum Chain of Pairs 
# A problem that introduces chaining optimization techniques and teaches sequential pair 
# selection algorithms using greedy approach for efficient relationship building and 
# dependency management operations. 
# Given pairs (a, b), find the maximum number of pairs that can form a chain where each 
# pair's first element is greater than the previous pair's second element using greedy selection. 
# This operation is fundamental in sequence optimization and dependency resolution where 
# you need to maximize valid connections while maintaining ordering constraints efficiently. 
# The technique uses end-value based greedy approach to sort pairs by second element and 
# select compatible pairs that maintain the chaining property. This concept is essential in 
# workflow management, task dependencies, and pipeline optimization where maximizing 
# sequential operations enables efficient process flow and optimal resource chaining in 
# dependency-aware systems. 
# This introduces chain optimization algorithms and sequential selection techniques that are 
# essential for dependency management and efficient relationship maximization 
# operations. 
# Your task: Implement greedy pair chaining using end-value sorting to maximize compatible 
# pair sequences with optimal dependency satisfaction. 
# Examples 
# Input: 
# pairs = [(5, 24), (15, 25), (27, 40), (50, 60)] 
# Output: 
# 3 
# Input: 
# pairs = [(1, 2), (2, 3), (3, 4)] 
# Output: 
# 2 
# 3. Schedule Tasks Without Overlap 
# A problem that teaches interval conflict resolution and demonstrates overlap elimination 
# algorithms using greedy approach for efficient scheduling and resource conflict minimization 
# operations. 
# Given start and end times of tasks, find the minimum number of tasks to remove so that 
# remaining tasks don't overlap using greedy conflict resolution. This operation is fundamental 
# in scheduling optimization and conflict resolution where you need to minimize task 
# removal while eliminating overlaps efficiently. The technique uses earliest end time greedy 
# approach to identify and retain non-overlapping tasks that maximize schedule utilization. 
# This concept is essential in resource scheduling, meeting planning, and system allocation 
# where resolving conflicts while minimizing disruption enables efficient resource utilization 
# and optimal schedule management in conflict-prone environments. 
# This teaches overlap resolution algorithms and conflict minimization techniques that are 
# crucial for scheduling optimization and efficient task conflict elimination operations. 
# Your task: Implement greedy overlap elimination using earliest end time strategy to 
# minimize task removal while achieving conflict-free scheduling with optimal retention. 
# Examples 
# Input: 
# intervals = [(1, 2), (2, 3), (3, 4), (1, 3)] 
# Output: 
# Remove 1 → Remaining 3 
# Input: 
# intervals = [(1, 2), (1, 2), (1, 2)] 
# Output: 
# Remove 2 → Remaining 1 
def min_coins(coins, amount):
    coins.sort(reverse=True)  # sort descending
    count = 0
    i = 0
    while amount > 0 and i < len(coins):
        if coins[i] <= amount:
            use = amount // coins[i]  # number of coins
            count += use
            amount -= use * coins[i]
        i += 1
    return count if amount == 0 else -1  # if exact amount cannot be formed

# Example
print(min_coins([1, 2, 5, 10], 23))  # Output: 5 (10+10+2+1)
print(min_coins([1, 5, 6, 9], 11))   # Output: 2 (6+5)
