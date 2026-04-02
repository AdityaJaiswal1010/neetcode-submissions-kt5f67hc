class Solution:
    def helper(self, nums, idx, dp,status):
        if idx >= len(nums):
            return 0
        
        if dp[idx][status] != -1:
            return dp[idx][status]
        ans=0
        if status:
            not_take = self.helper(nums, idx + 1, dp,status)
            take= nums[idx] + self.helper(nums,idx+1,dp,0)
            ans=max(not_take,take)
        else:
            take = self.helper(nums, idx+1, dp,1)
            ans=take
        
        dp[idx][status] = ans
        return dp[idx][status]
    
    def rob(self, nums):
        dp =  [[-1] * 2 for _ in range(len(nums))]
        return self.helper(nums, 0, dp,1)