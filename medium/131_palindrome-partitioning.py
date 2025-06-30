# 131. Palindrome Partitioning
# Difficulty: Medium

# Link: https://leetcode.com/problems/palindrome-partitioning/description/

# choice
#   we explore each substring starting from each index
# constraint
#   we check if substrings are palindromes and append to the current list if so
# goal
#   if our path reaches the string length, we have a solution
def solution(self, s: str) -> list[list[str]]:
    
    sol = []
    def backtrack(start, path):
        if start == len(s):
            sol.append(path.copy()) 
            return
        
        for i in range(start + 1, len(s) + 1):
            substring = s[start:i]
            if substring == substring[::-1]:
                path.append(substring)
                backtrack(i + 1, path)
                path.pop()
    
    backtrack(0, [])
    return sol


def main():
    pass

if __name__ == "__main__":
    main()
