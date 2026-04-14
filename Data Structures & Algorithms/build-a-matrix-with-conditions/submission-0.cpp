class Solution {
public:
    bool toposort(int& k,
                  vector<unordered_set<int>>& adj,
                  vector<unordered_set<int>>& inorder,
                  vector<int>& ans) {

        queue<int> q;
        int count = 0;

        for(int i = 0; i < k; i++){
            if(inorder[i].size() == 0){
                q.push(i);
                ans[i] = count++;
            }
        }

        while(!q.empty()){
            int curr = q.front();
            q.pop();

            for(auto next : adj[curr]){
                inorder[next].erase(curr);

                if(inorder[next].size() == 0){
                    q.push(next);
                    ans[next] = count++;
                }
            }
        }

        return count == k;
    }

    vector<vector<int>> buildMatrix(int k,
                                   vector<vector<int>>& rowConditions,
                                   vector<vector<int>>& colConditions) {

        vector<int> row(k);
        vector<int> col(k);

        vector<unordered_set<int>> adjr(k);
        vector<unordered_set<int>> inorderr(k);

        for(auto &c : rowConditions){
            int u = c[0] - 1;
            int v = c[1] - 1;

            adjr[u].insert(v);
            inorderr[v].insert(u);
        }

        if(!toposort(k, adjr, inorderr, row))
            return {}; 


        vector<unordered_set<int>> adjc(k);
        vector<unordered_set<int>> inorderc(k);

        for(auto &c : colConditions){
            int u = c[0] - 1;
            int v = c[1] - 1;

            adjc[u].insert(v);
            inorderc[v].insert(u);
        }

        if(!toposort(k, adjc, inorderc, col))
            return {};


        vector<vector<int>> ans(k, vector<int>(k, 0));

        for(int i = 0; i < k; i++){
            ans[row[i]][col[i]] = i + 1;
        }

        return ans;
    }
};