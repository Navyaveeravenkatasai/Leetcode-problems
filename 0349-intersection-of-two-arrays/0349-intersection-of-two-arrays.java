class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> s = new HashSet<>();

        Set<Integer> set1 = new HashSet<>();
        for (int num : nums1)  set1.add(num);

        Set<Integer> set2 = new HashSet<>();        
        for (int num : nums2) set2.add(num);

        for (int i : nums1) {
            if (set2.contains(i)) s.add(i);
        }
        int[] res = new int[s.size()]; int c=0;
        for (int i : s) {
            res[c++] = i;
        }
        return res ;
    }
}