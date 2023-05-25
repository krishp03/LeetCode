class ValidParentheses:

    def isValid(self, s: str) -> bool:
        def isOpen(c: str) -> bool:
            return c == '(' or c == '[' or c == '{'

        def corresponding(open: str, close: str) -> bool:
            if open == '(' and  close != ')':
                return False
            if open == '[' and  close != ']':
                return False
            if open == '{' and  close != '}':
                return False
            return True

        stack = []
        for char in s:
            if isOpen(char):
                stack.append(char)
            else:
                if(len(stack) == 0 or not corresponding(stack.pop(), char)):
                    return False
        return len(stack) == 0
