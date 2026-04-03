from collections import deque

class Solution:
    def helper(self, s, start, idx, dp, curr):

        # remove heading zeros
        while curr:
            if curr[0] == '0':
                curr.popleft()
            else:
                break

        if idx == len(s):
            return 1

        if dp[start][idx] != -1:
            return dp[start][idx]

        ans = 0
        curr.clear()  # ensure fresh window each call

        for i in range(idx, len(s)):

            curr.append(s[i])

            mylst = list(curr)
            temp = int(''.join(mylst))

            if temp == 0:
                break

            if temp <= 26:
                take = self.helper(s, i + 1, i + 1, dp, deque())
                ans += take
            else:
                break

        dp[start][idx] = ans
        return dp[start][idx]

    def numDecodings(self, s: str):

        if not s or s[0] == '0':
            return 0

        dp = [[-1] * len(s) for _ in range(len(s))]
        curr = deque()

        return self.helper(s, 0, 0, dp, curr)