# 150. Evaluate Reverse Polish Notation
# Difficulty: Medium

# Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

# neetcode says this is a stack question
# starting by learning what reverse polish notation is
# implementation: keep pushing onto the stack
# when we see an operator we pop two nums, second popped is left side of operator
# when evaluating operators, is there a faster way than 4 ifs?
# I think switch statements are faster? they're cleaner at least, let's try it for now

# when we reach the last element, it will always be an operator and we just do
# one pop and the operation
# not clean, but for now I'll just repeat code
# actually we only pop twice for the first operation, let's fix that

# Popping from an empty list, why

# I'm goofy, we can just push the result back onto the stack
# removes the need for edge case checking and a solution var
# still popping from an empty list
# isnumeric() can't check negative #s, remove - from all nums before checking

# time complexity: O(n)
# space complexity: O(n)
# time to solve: 45 min

def solution(tokens: list[str]) -> int:

    stack = []
    for char in tokens:
        if char.lstrip("-").isnumeric():
            stack.append(int(char))
            continue

        op2 = stack.pop()
        op1 = stack.pop()

        match char:
            case "+":
                sol = op1 + op2
            case "-":
                sol = op1 - op2
            case "*":
                sol = op1 * op2
            case "/":
                sol = int(op1 / op2)
        stack.append(sol)

    return stack[-1]



def main():
    tokens = ["2","1","+","3","*"]# 9
    print(solution(tokens))

    tokens = ["4","13","5","/","+"]# 6
    print(solution(tokens))

    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]# 22
    print(solution(tokens))

if __name__ == "__main__":
    main()
