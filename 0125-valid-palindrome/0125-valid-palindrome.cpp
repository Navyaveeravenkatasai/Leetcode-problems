class Solution {
public:
    bool isPal(const string& s, int left, int right) {
        // Move left and right to next alphanumeric character
        while (left < right && !isalnum(s[left])) left++;
        while (left < right && !isalnum(s[right])) right--;

        // Base case
        if (left >= right) return true;

        // Compare characters (case-insensitive)
        if (tolower(s[left]) != tolower(s[right])) return false;

        return isPal(s, left + 1, right - 1); // Recursive step
    }
    bool isPalindrome(string s) {
        return isPal(s, 0, s.length() - 1);   
    }
};