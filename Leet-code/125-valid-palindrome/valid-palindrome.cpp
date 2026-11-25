class Solution {
public:
    bool isPalindrome(string s) {
        string res = "";
        for(char ch : s){
            if(ch>= 'A' && ch <= 'Z'){
                res += tolower(ch);
            }
            else if(ch >= 'a' && ch <= 'z'){
                res+= ch;
            }
            else if(ch>='0' && ch <= '9'){
                res+= ch;

            }
        }
        int l=0;
        int r = res.size()-1;

        while(l<r){
            if(res[l] != res[r]){
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
};