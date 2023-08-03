class CoinChange:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [0] + [-1] * (amount)
        for i in range(1, amount+1):
            for coin_val in coins:
                diff_index = i-coin_val
                if diff_index >= 0 and dp[diff_index] != -1:
                    coins_used = dp[diff_index] + 1
                    dp[i] = coins_used if dp[i] == -1 else min(coins_used, dp[i])
                    
        return dp[amount]
