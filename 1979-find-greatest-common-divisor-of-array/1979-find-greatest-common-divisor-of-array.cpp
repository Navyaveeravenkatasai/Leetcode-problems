class Solution {
public:
    int findGCD(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int n1=nums[0];
        int n2=nums[nums.size()-1];

        while(n1>0 && n2>0){
            if(n1>n2) n1=n1%n2;
            else n2=n2%n1;
        }
        if(n1==0) return n2;
        return n1;
    }
};