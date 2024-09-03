def validParenthesis(input):
    stack = []
    if len(input) == 1:
        return False
    for i in input:
        if i == ")":
            if len(stack) == 0:
                return False
            elif stack[len(stack) - 1] == "(":
                stack.pop()
            else:
                return False
        if i == "]":
            if len(stack) == 0:
                return False
            elif stack[len(stack) - 1] == "[":
                stack.pop()
            else:
                return False
        if i == "}":
            if len(stack) == 0:
                return False
            elif stack[len(stack) - 1] == "{":
                stack.pop()
            else:
                return False
        if i == "(" or i == "[" or i == "{":
            stack.append(i)
        if len(stack) == 0:
            return True
        else:
            return False

            

print(validParenthesis("(("))