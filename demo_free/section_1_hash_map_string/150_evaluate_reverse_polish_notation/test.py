def evalRPN(tokens):
    stack = []

    for token in tokens:
        if token in "+-*/":
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                stack.append(a+b)
            elif token == "-":
                stack.append(a-b)
            elif token == "*":
                stack.append(a*b)
            else:
                stack.append(int(a/b))
        else:
            stack.append(int(token))

    return stack[0]


# 输入: ["2","1","+","3","*"]
# 输出: 9

# 解释: (2 + 1) * 3 = 9