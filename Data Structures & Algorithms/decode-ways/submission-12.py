from collections import deque
from typing import List

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

        # ❗ important fix: '0' cannot be decoded alone
        if s[idx] == '0':
            return 0

        curr.append(s[idx])

        mylst = list(curr)
        temp = int(''.join(mylst))

        if temp > 26:
            curr.pop()
            return 0

        ans = 0

        # take single digit
        take = self.helper(s, idx + 1, idx + 1, dp, deque())
        ans += take

        # take two digits if possible
        if idx + 1 < len(s):
            curr.append(s[idx + 1])

            mylst = list(curr)
            temp = int(''.join(mylst))

            if temp <= 26:
                nottake = self.helper(s, idx + 2, idx + 2, dp, deque())
                ans += nottake

            curr.pop()

        curr.pop()

        dp[start][idx] = ans
        return dp[start][idx]

    def numDecodings(self, s: str) -> int:

        if not s or s[0] == '0':
            return 0

        dp = [[-1] * len(s) for _ in range(len(s))]
        curr = deque()

        return self.helper(s, 0, 0, dp, curr)