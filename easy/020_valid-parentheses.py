# 020. Valid Parentheses
# Difficulty: Easy

# Link: https://leetcode.com/problems/valid-parentheses/description/

# seems simple, just push left braces onto stack, pop when right brace,
# check if it matches
# lot of edge cases, single braces, start with right brace, etc.
# lot of debugging
# time to solve: 15 min
# time complexity: O(n)
# space complexity: O(n)
def solution(s: str) -> bool:
    
    stack = []
    if len(s) % 2 != 0:
        return False
    for char in s:
        if char == "{" or char == "(" or char == "[":
            stack.append(char)
            continue
        elif not stack:
            return False
        check = stack.pop()
        if check == "{" and char != "}":
            return False
        if check == "(" and char != ")":
            return False
        if check == "[" and char != "]":
            return False
        
    return not stack

def main():
    s = "(]" #false
    print(solution(s))

    s = "()[]{}"# true
    print(solution(s))


if __name__ == "__main__":
    main()
