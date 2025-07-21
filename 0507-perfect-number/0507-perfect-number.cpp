class Solution {
public:
    bool checkPerfectNumber(int num) {
        int dup=num;
        int sum = 0; // to calculate sum of all its positive divisors
        for(int i=1; i<num; i++) {
            if(num%i == 0) {
                sum = sum + i;
            }
        }

        if(sum == num) {
            return true;
        }
        else{
            return false;
        }
    }
};