# 678. Valid Parenthesis String
# Difficulty: Medium

# Link: https://leetcode.com/problems/valid-parenthesis-string/description/

# my first thought is to count left, right, and asterisks
#   if left == right, then all asterisks are empty
#       doesn't work, *)(*
# we can brute force by backtracking, but that's very inefficient
# actually we can use two stacks
#   first loop, we keep track of the left parentheses and stars, popping while there's right parentheses
#   after going through the string, if the stacks aren't empty then we need to match for the rest of the right parentheses
#       we need to make sure the left parentheses are before the stars too(right paren)
def solution(self, s: str) -> bool:
    left = []
    stars = []
    for i in range(len(s)):
        if s[i] == "(":
            left.append(i)
        elif s[i] == "*":
            stars.append(i)
        else:
            if not left and not stars:
                return False
            if left:
                left.pop()
            else:
                stars.pop()

    while left and stars:
        if left[-1] < stars[-1]:
            left.pop()
            stars.pop()
        else:
            break

    return len(left) == 0

def main():
    pass

if __name__ == "__main__":
    main()
