class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #    MAX VALUE or math.inf  ---- since 0 to amount = amount + 1
        dp = [amount + 1] * (amount + 1)
        # base case, zero sum always takes no coins
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                # can be picked as an option
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])

        return dp[amount] if dp[amount] != amount + 1 else -1 



        