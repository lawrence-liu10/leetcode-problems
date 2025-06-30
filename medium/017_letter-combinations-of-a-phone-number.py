# 017. Letter Combinations Of A Phone Number
# Difficulty: Medium

# Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

# we can start by making a dictionary containing each of the letter/number combinations
# choice
#   for each digit, we can choose any of the corresponding letters
# constraints
#   none, just iterate through the letters for each num
# goal
#   when a string reaches the length of the digit string, it's a solution
def solution(self, digits: str) -> list[str]:

    map = {
        '2': ['a','b','c'],
        '3': ['d','e','f'],
        '4': ['g','h','i'],
        '5': ['j','k','l'],
        '6': ['m','n','o'],
        '7': ['p','q','r','s'],
        '8': ['t','u','v'],
        '9': ['w','x','y','z']
    }
    sol = []
    if not digits:
        return sol
    
    def backtrack(str, i):
        if len(str) == len(digits):
            sol.append(str)
            return
        
        for char in map[digits[i]]:
            backtrack(str + char, i + 1)
    
    backtrack("", 0)
    return sol
    



def main():
    pass

if __name__ == "__main__":
    main()
