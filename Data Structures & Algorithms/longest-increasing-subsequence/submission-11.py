import sys
sys.setrecursionlimit(10**7)
class Solution:
    def help(self, nums, dp, prev, index):

        if index >= len(nums):
            return 0

        if dp[index][prev + 1] != -1:
            return dp[index][prev + 1]

        nottake = self.help(nums, dp, prev, index + 1)

        take = 0
        if prev == -1 or nums[prev] < nums[index]:
            take = 1 + self.help(nums, dp, index, index + 1)

        dp[index][prev + 1] = max(take, nottake)

        return dp[index][prev + 1]


    def lengthOfLIS(self, nums):

        dp = [[-1] * (len(nums) + 1) for _ in range(len(nums) + 1)]

        return self.help(nums, dp, -1, 0)