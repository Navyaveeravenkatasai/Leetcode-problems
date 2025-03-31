import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        java.util.Map<Character, Character> closetoopen = Map.of(
            ')', '(',
            '}', '{',
            ']', '['
        );

        for (char c : s.toCharArray()) {
            if (closetoopen.containsKey(c)) {
                if (!stack.isEmpty() && stack.peek() == closetoopen.get(c)) {
                    stack.pop();
                } else {
                    return false;
                }
            } else {
                stack.push(c);
            }
        }
        return stack.isEmpty();
    }
}
