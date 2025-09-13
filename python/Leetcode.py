# class Solution:
#     def maxTotalFruits(self, fruits, startPos, k):
#         max_total = 0
#         left = 0
#         total = 0
#         n = len(fruits)

#         for right in range(n):
#             total += fruits[right][1]  # Add fruits at current right pointer

#             # Shrink the window if it's too far to walk
#             while left <= right:
#                 left_pos = fruits[left][0]
#                 right_pos = fruits[right][0]

#                 # Cost when going left first or right first
#                 left_first = abs(startPos - left_pos) + (right_pos - left_pos)
#                 right_first = abs(startPos - right_pos) + (right_pos - left_pos)

#                 if min(left_first, right_first) <= k:
#                     break

#                 total -= fruits[left][1]
#                 left += 1

#             max_total = max(max_total, total)

#         return max_total
class Solution(object):
    def maxProfit(self, prices, strategy, k):
        n = len(prices)
        original = sum(strategy[i] * prices[i] for i in range(n))
        half = k // 2
        leftDelta  = [-strategy[i] * prices[i] for i in range(n)]
        rightDelta = [(1 - strategy[i]) * prices[i] for i in range(n)]
        prefixLeft  = [0] * (n + 1)
        prefixRight = [0] * (n + 1)
        for i in range(n):
            prefixLeft[i+1]  = prefixLeft[i]  + leftDelta[i]
            prefixRight[i+1] = prefixRight[i] + rightDelta[i]
        bestDelta = 0
        for s in range(n - k + 1):
            leftSum  = prefixLeft[s + half] - prefixLeft[s]
            rightSum = prefixRight[s + k]   - prefixRight[s + half]
            delta = leftSum + rightSum
            if delta > bestDelta:
                bestDelta = delta
        return original + bestDelta