class ValidParentheses {
    public boolean isValid(String s) {
        Stack<Character> startBrackets = new Stack<>();
        char[] chars = s.toCharArray();
        for(char c : chars) {

            if(isOpening(c)) {
                startBrackets.push(c);
            }

            else {
                if(startBrackets.isEmpty()) {
                    return false;
                }
                if(!isCorresponding(startBrackets.pop(), c))
                    return false;
            }
        }
        return startBrackets.size() == 0;
    }

    private boolean isCorresponding(char open, char close) {
        if(open == '(') {
            return close == ')';
        } else if(open == '{') {
            return close == '}';
        }
        return close == ']';
    }

    private boolean isOpening(char c) {
        return (c == '(' || c == '{' || c == '[');
    }
}
