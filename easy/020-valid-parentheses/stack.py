def valid_parentheses(s: str)->bool:
    stack = []
    pair = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    
    for char in s:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack:
                return False
            if stack[-1] == pair[char]:
                stack.pop()
            else:
                return False
    return not stack

print(valid_parentheses("()"))
print(valid_parentheses("()[]{}"))
print(valid_parentheses("(]"))
print(valid_parentheses("([)]"))
print(valid_parentheses("{[]}"))
print(valid_parentheses("({[]})"))
print(valid_parentheses(")"))
print(valid_parentheses("([}"))