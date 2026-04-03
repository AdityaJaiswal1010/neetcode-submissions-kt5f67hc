class Solution:
    def help(self, coins, amount, dp, index):

        if amount == 0:
            return 0

        if amount < 0 or index < 0:
            return 1000000  # number cannot be formed

        if dp[index][amount] != -1:
            return dp[index][amount]

        nottake = float('inf')

        if amount - coins[index] >= 0:
            nottake = 1 + self.help(coins, amount - coins[index], dp, index)

        take = self.help(coins, amount, dp, index - 1)

        dp[index][amount] = min(take, nottake)

        return dp[index][amount]


    def coinChange(self, coins, amount):

        coins.sort()

        dp = [[-1] * (amount + 1) for _ in range(len(coins))]

        ans = self.help(coins, amount, dp, len(coins) - 1)

        if ans >= 1000000:
            return -1

        return ans