def coinChange(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0  # base case

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != amount + 1 else -1

# 输入: coins = [1, 2, 5], amount = 11
# 输出: 3
# 解释: 11 = 5 + 5 + 1


# 输入: coins = [2], amount = 3
# 输出: -1