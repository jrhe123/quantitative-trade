def isValid(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}

    for char in s:
        print("stack: ", stack)
        if char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:
            stack.append(char)

    return not stack


# 输入: "()[]{}"   输出: True  
# 输入: "([)]"     输出: False  
# 输入: "{[]}"     输出: True

ans = isValid('()[]{}')
print(ans)
