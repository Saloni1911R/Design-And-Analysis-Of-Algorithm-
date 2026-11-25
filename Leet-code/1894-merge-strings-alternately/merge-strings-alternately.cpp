class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int n1=word1.size();
        int n2=word2.size();
        string res="";
        int i = 0;
        while(i<n1 && i<n2){
            res+=word1[i];
            res+=word2[i];
            i++;
        }
        while(i<n1){
            res+=word1[i];
            i++;
        }
        while(i<n2){
            res+=word2[i];
            i++;
        }
        return res;
    }
};