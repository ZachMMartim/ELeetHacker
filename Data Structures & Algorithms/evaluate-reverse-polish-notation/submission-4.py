class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operatorset = set({'+', '-', '*', '/'})
        for token in tokens:
            if token in operatorset:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "/":
                    stack.append(int(a / b))   
            else:
                stack.append(int(token))

        return stack[0]
            


        