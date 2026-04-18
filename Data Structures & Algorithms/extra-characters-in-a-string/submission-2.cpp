class Solution {
public:
    int helper(string& s, unordered_set<string>& st, vector<vector<int>>& dp, int idx, int prev, string curr) {
        if (idx >= s.length()) {
            if (st.find(curr) != st.end())
                return 0;
            return (int)curr.size(); // extra chars = length of unmatched curr
        }
        if (dp[idx][prev + 1] != -1)
            return dp[idx][prev + 1];

        // Option 1: don't break at idx, extend curr
        int nottake = helper(s, st, dp, idx + 1, prev, curr + s[idx]);

        // Option 2: break at idx
        int take = 0;
        if (st.find(curr) != st.end()) {
            // curr is a valid word, no extra chars for it
            take = helper(s, st, dp, idx + 1, idx, string(1, s[idx]));
        } else {
            // curr is invalid, all its chars are extra
            take = (int)curr.size() + helper(s, st, dp, idx + 1, idx, string(1, s[idx]));
        }

        return dp[idx][prev + 1] = min(take, nottake);
    }

    int minExtraChar(string s, vector<string>& dictionary) {
        unordered_set<string> st(dictionary.begin(), dictionary.end());
        vector<vector<int>> dp(s.length() + 1, vector<int>(s.length() + 1, -1));
        return helper(s, st, dp, 0, -1, "");
    }
};