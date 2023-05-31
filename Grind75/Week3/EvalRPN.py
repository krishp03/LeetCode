class EvalRPN:
    def evalRPN(self, tokens: List[str]) -> int:
        def evaluate(num2:int, num1: int, operator: str) -> int:
            match operator:
                case '+':
                    return num1 + num2
                case '-':
                    return num1 - num2
                case '*':
                    return num1 * num2
                case '/':
                    return int(num1 / num2)
            return -1 # Never reaches uneless error in input        
        
        stack = []
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                stack.append(evaluate(stack.pop(), stack.pop(), token))
            else:
                stack.append(int(token))
        return stack[0]
