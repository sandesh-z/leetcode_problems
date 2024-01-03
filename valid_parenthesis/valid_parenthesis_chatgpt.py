def isValid(s):
    stack = []
    bracket_mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_mapping.values():
            # If the character is an opening bracket, push it onto the stack
            stack.append(char)
        elif char in bracket_mapping.keys():
            # If the character is a closing bracket
            if stack and stack[-1] == bracket_mapping[char]:
                # Check if the stack is not empty and the top of the stack matches the corresponding opening bracket
                stack.pop()
            else:
                return False
        else:
            # If the character is neither an opening nor a closing bracket, ignore it
            continue

    # The string is valid if the stack is empty at the end
    return not stack