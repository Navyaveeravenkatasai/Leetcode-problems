class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        unordered_set<int> res;
        for(int num:nums){
            if (res.find(num) != res.end()) {
            return num;
        } else {
            res.insert(num);
        }
        }
        return -1;
    }
};