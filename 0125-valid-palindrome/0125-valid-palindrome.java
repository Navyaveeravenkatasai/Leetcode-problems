class Solution {
    public static boolean checkpalindrome(String s){
        int left =0;
        int right=s.length() -1;
        while(left<right){
            char currFirst = s.charAt(left);
        	char currLast = s.charAt(right);
            if(currFirst != currLast){
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    public boolean isPalindrome(String s) {
        StringBuilder sb =new StringBuilder();
        for(int i=0;i<s.length();i++){
            char ch = s.charAt(i);
            if (Character.isLetter(ch) || Character.isDigit(ch)){
                sb.append(ch);
            }
        }
        String result =sb.toString();
        result = result.toLowerCase();
        if (checkpalindrome(result)){
            return true;
        }
        return false;
    }
}