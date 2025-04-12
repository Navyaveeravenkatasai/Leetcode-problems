class Solution {
    boolean isvowel(char ch){
        if(
            ch=='a' ||
            ch=='e' ||
            ch=='i' ||
            ch=='o' ||
            ch=='u' ||
            ch=='A' ||
            ch=='E' ||
            ch=='I' ||
            ch=='O' ||
            ch=='U' 
        )
        return true;
        
        return false;
    }
    public String reverseVowels(String s) {
        int i=0;
        int j=s.length()-1;
        char [] arr = s.toCharArray();

        while(i<j){
            if(!isvowel(arr[i]))i++;
            if(!isvowel(arr[j]))j--;
            if(isvowel(arr[i])  && isvowel(arr[j]))
            {
                char temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;

                i++;
                j--;
            }
        }
        return new String(arr);
    }
}