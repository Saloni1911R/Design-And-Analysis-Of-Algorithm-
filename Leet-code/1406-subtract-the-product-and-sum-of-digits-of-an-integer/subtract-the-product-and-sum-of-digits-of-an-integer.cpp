class Solution {
public:
    int subtractProductAndSum(int n) {
        int a = 0;
        int sum = 0;
        int multi = 1;
        while(n>0){
            a = n % 10;
            n /= 10;
            sum += a;
            multi *= a;
        }
        return multi - sum;
    }
};