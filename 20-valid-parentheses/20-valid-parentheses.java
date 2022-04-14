class Solution {
    public boolean isValid(String s) {
        char sChars[] = s.toCharArray();
        Stack<Character> stack = new Stack<Character>();
        for (int i = 0; i < sChars.length; i++){
            if (sChars[i] == '(' || sChars[i] == '{' || sChars[i] == '[')
                stack.push(sChars[i]);
            else {
                if (stack.isEmpty())
                    return false;
                if (sChars[i] == ')' && stack.pop() != '(')
                    return false;
                if (sChars[i] == ']' && stack.pop() != '[')
                    return false;
                if (sChars[i] == '}' && stack.pop() != '{')
                    return false;
            }
        }
        return stack.isEmpty();
    }
}

