# 647. Palindromic Substrings
# Difficulty: Medium

# Link: https://leetcode.com/problems/palindromic-substrings/description/

# we can use the exact same approach, but any time the function to expand is called,
#   we just increment our count
# need to revisit with dp approach for longest and this question
def solution(self, s: str) -> int:

    sol = 0
    def expand(s, left, right) -> int:
        nonlocal sol
        while (left >= 0 and right < len(s) and s[left] == s[right]):
            sol += 1
            left -= 1
            right += 1

    start = 0
    end = 0
    for i in range(len(s)):
        expand(s, i, i)
        expand(s, i, i + 1)
    
    return sol

def main():
    pass

if __name__ == "__main__":
    main()
