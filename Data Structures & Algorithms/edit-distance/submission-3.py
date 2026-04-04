class Solution:
    def helper(self, word1, word2, dp, idx1, idx2):
        if idx1 == len(word1) and idx2 == len(word2):
            return 0
        
        if idx1 == len(word1):
            return len(word2) - idx2
        
        if idx2 == len(word2):
            return len(word1) - idx1
        
        if dp[idx1][idx2] != -1:
            return dp[idx1][idx2]
        
        if word1[idx1] == word2[idx2]:
            ans = self.helper(word1, word2, dp, idx1 + 1, idx2 + 1)
        else:
            # insert, delete, replace
            insert_op = 1 + self.helper(word1, word2, dp, idx1, idx2 + 1)
            delete_op = 1 + self.helper(word1, word2, dp, idx1 + 1, idx2)
            replace_op = 1 + self.helper(word1, word2, dp, idx1 + 1, idx2 + 1)
            
            ans = min(insert_op, delete_op, replace_op)
        
        dp[idx1][idx2] = ans
        return ans

    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 or not word2:
            return max(len(word1), len(word2))
        
        dp = [[-1] * len(word2) for _ in range(len(word1))]
        return self.helper(word1, word2, dp, 0, 0)