def isValid(s:str)->bool:
    stack = []
    for item in s:
        if(item=="("):
            stack.append(")")
        elif(item=="{"):
            stack.append("}")
        elif(item=="["):
            stack.append("]")  
        elif(item=="]" or item ==")" or item=="}"):
            if not stack:
                return False
            else:
                if(item!=stack[-1]):
                    return False
                else:
                    stack.pop()
    if not stack:
        return True
    else:
        return False            
    
 
print(isValid("([)]"))    