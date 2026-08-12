class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in '+-*/':
                first = stack.pop()
                second = stack.pop()
                if i == '+':
                    stack.append(first+second)
                elif i == '-':
                    stack.append(second-first)
                elif i == '*':
                    stack.append(first*second)
                else:
                    if first == 0 or second == 0:
                        stack.append(0)
                    else:
                        stack.append(int(second/first))

                
            else:
                stack.append(int(i))
        
        return stack[-1]
        