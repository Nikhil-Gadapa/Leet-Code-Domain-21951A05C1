from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1 or k == 0:
            return 0

        # If k is large enough, the problem can be treated as an unlimited transaction case
        if k >= n // 2:
            return sum(max(prices[i + 1] - prices[i], 0) for i in range(n - 1))

        # Initialize buy and sell arrays
        buy = [-prices[0]] * k
        sell = [0] * k

        for price in prices[1:]:
            for i in range(k):
                buy[i] = max(buy[i], (sell[i - 1] if i > 0 else 0) - price)
                sell[i] = max(sell[i], buy[i] + price)

        return sell[-1]

# Example usage:
# solution = Solution()
# result = solution.maxProfit(2, [3,2,6,5,0,3])
# print(result)
