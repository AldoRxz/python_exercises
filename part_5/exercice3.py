class ValidParentheses:
    def is_valid(self, s):
        stack = []
        parentheses_map = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in parentheses_map.values():
                stack.append(char)
            elif char in parentheses_map.keys():
                if not stack or stack.pop() != parentheses_map[char]:
                    return False
            else:
                return False

        return not stack

# Ejemplo de uso
validator = ValidParentheses()

# Casos de prueba
print(validator.is_valid("()"))       # True
print(validator.is_valid("()[]{}"))   # True
print(validator.is_valid("[)"))       # False
print(validator.is_valid("({[)]"))    # False
print(validator.is_valid("{{{"))      # False
