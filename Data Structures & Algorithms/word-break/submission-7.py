class Solution:
    def helper(self, s,dic,curr,idx,prev,dp):
        if idx==len(s):
            if not curr or ''.join(curr) in dic:
                return True
            else:
                return False
        if dp[idx][prev+1]!=-1:
            return dp[idx][prev+1]
        ans=False
        for i in range (idx,len(s)):
            curr.append(s[i])
            if ''.join(curr) in dic:
                take=self.helper(s,dic,[],i+1,i+1,dp)
                ans=ans or take
        dp[idx][prev+1]=ans
        return dp[idx][prev+1]
        
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dic=set()
        for i in wordDict:
            dic.add(i)
        curr=[]
        dp=[[-1]* (len(s)+1) for _ in range(len(s)+1)]
        return self.helper(s,dic,curr,0,-1,dp)