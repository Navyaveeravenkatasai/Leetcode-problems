class Solution {
    public int removeDuplicates(int[] nums) {
        int len = nums.length;
        int j=1;
        for(int i=1;i<len;i++){
            if(nums[i] != nums[i - 1]){
                nums[j] = nums[i];
                j = j+1;
            }
        }
        return j;
    }
}