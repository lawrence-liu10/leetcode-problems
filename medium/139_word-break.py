# 139. Word Break
# Difficulty: Medium

# Link: https://leetcode.com/problems/word-break/

# for this question, we can check at each starting point if it matches a word from the set,
#   and also recurse on the leftover portion
# if a substring is valid, we'll mark it as valid and vice versa before continuing
def solution(self, s: str, wordDict: list[str]) -> bool:
    words = set(wordDict)
    memo = {}

    def dp(str):
        if str in memo:
            return memo[str]
        if not str:
            return True
        for i in range(1, len(str) + 1):
            if str[:i] in words and dp(str[i:]):
                memo[str] = True
                return True
        memo[str] = False
        return False
    
    return dp(s)

def main():
    pass

if __name__ == "__main__":
    main()
