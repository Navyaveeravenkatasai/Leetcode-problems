class Solution {
    public int removeDuplicates(int[] nums) {
        int len = nums.length;
        int i=0;
        for(int j=1;j<len;j++){
            if(nums[i]!=nums[j]){
                nums[i+1]=nums[j];
                i++;
            }
        }
        return i+1;
    }
}