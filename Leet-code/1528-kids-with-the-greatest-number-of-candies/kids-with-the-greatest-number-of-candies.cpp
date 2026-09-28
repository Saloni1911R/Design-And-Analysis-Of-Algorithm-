class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        vector<bool> ans;
        int largest = 0;
        int n = candies.size();

        for(int i = 0; i<n; i++){
            largest = max(largest,candies[i]);
        }  

        for(int i =0; i<n; i++){
            if(candies[i]+extraCandies >= largest){
                ans.push_back(true);
            }
            else{
                ans.push_back(false);
            }
        }return ans;
    }
    
};