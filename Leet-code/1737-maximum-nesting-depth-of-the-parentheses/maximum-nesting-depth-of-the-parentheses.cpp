class Solution {
public:
    int maxDepth(string s) {
        int curr = 0;
        int maxpar = 0;
        for(char ch:s){
            if(ch == '('){
                curr += 1;
                if(curr > maxpar){
                    maxpar = curr;
                }
            }
            else if(ch == ')'){
                curr -= 1;
            }
        }
        return maxpar;
    }
};