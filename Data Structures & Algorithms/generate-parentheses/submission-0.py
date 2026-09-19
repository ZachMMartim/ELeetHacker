class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = []

        def backtrack(leftP, rightP): 
            if leftP == rightP == n:
                result.append("".join(stack))
                return
            
            if leftP < n: 
                stack.append("(")
                backtrack(leftP + 1, rightP)
                stack.pop()
            if leftP > rightP:
                stack.append(")")
                backtrack(leftP, rightP + 1)
                stack.pop()
                 

        backtrack(0, 0)
        return result

        