class Solution {
    public boolean isSubsequence(String s, String t) {

        int l = 0;
        int r = s.length() -1 ;

        int sl = 0;
        int sr = t.length() - 1;

        while(l<=r && sl<=sr){
            if(s.charAt(l) == t.charAt(sl)){
                l++;
            }
            sl++;

            if(sl > sr && (r-l) == 0)
            return false;

            if(s.charAt(r) == t.charAt(sr)){
                r--;
            }
            sr--;
        } 

        return r<l;
    }
}