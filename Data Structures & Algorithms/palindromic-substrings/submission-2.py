class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0

        # odd length palindrome
        for i in range(len(s)):
            l = i
            r = i
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                ans += 1
                l -= 1
                r += 1

        # even length palindrome
        for i in range(len(s)):
            l = i
            r = i + 1
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                ans +=1
                l -= 1
                r += 1

        return ans