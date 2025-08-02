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

# bottom up approach
# in this case, an empty string is always in the word list
#   otherwise, we'll loop through our string and if a word exists in word dict, and 
#   appears after another previously valid word, it's valid
# if at the end the dp array is true, then it's only made up of words from wordDict
def solution(self, s: str, wordDict: list[str]) -> bool:
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break
    
    return dp[len(s)]

def main():
    pass

if __name__ == "__main__":
    main()
