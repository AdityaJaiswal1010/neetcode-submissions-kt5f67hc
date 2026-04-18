class Solution {
public:
    int maxTurbulenceSize(vector<int>& arr) {

        if(arr.size()==1) return 1;

        int ans = 1;

        // PASS 1:
        // even index -> greater
        // odd index -> smaller
            int curr = 1;

            for(int i=1;i<arr.size();i++){

                if(i%2==0){
                    if(arr[i] > arr[i-1]) curr++;
                    
                    else curr = 1;
                }
                else{
                    if(arr[i] < arr[i-1]) curr++;
                
                    else curr = 1;
                }

                ans = max(ans,curr);
            }
    


        // PASS 2:
        // even index -> smaller
        // odd index -> greater
        
        curr = 1;

            for(int i=1;i<arr.size();i++){

                if(i%2==0){
                    if(arr[i] < arr[i-1]) curr++;
                    
                    else curr = 1;
                }
                else{
                    if(arr[i] > arr[i-1]) curr++;
                    
                    else curr = 1;
                }

                ans = max(ans,curr);
            }
        

        return ans;
    }
};