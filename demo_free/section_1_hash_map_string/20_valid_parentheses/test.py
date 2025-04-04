def isValid(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in mapping:
            if stack[-1] == mapping[char]:
                return False

            stack.pop()
        else:
            stack.append(char)

    return not stack