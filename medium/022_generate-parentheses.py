# 022. Generate Parentheses
# Difficulty: Medium

# Link: https://leetcode.com/problems/generate-parentheses/

# generate well-formed parentheses,
# n <= 8, should we make a stack for each n?
# for each new n, we can either pop and close or add a ( to the stack
# how do we code this? recursion? idk how to do iteratively
# each step has multiple possible substeps

# conditions:
# if # left paren = # right = n, add to solutions
# if left < n, add a left
# if right < left, add right

# current solution has 5 outputs, but way too many parentheses
# after each call to recursive, we need to pop to explore the other paths
# time to solve: 40 min
# space complexity: O(n)
# time complexity: could not think of it, chatgpt says O(4^n/sqrt(n))
def solution(n: int) -> list[str]:

    stack = []
    sols = []

    def recursive(left, right):
        if left == right == n:
            sols.append("".join(stack))
            return

        if left < n:
            stack.append("(")
            recursive(left + 1, right)

        if right < left:
            stack.append(")")
            recursive(left, right + 1)

    recursive(0,0)
    return sols


def main():
    pass

if __name__ == "__main__":
    main()
