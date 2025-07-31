# 091. Decode Ways
# Difficulty: Medium

# Link: https://leetcode.com/problems/decode-ways/description/

# for this question, let's solve it like this
#   any substring starting with a zero is invalid
#   we'll then recursively check if each number can be used, or if each double number can be used
def solution(self, s: str) -> int:
    
    count = 0
    def dfs(s):
        nonlocal count
        if not s:
            count += 1
            return
        if s[0] == '0':
            return 0
        
        dfs(s[1:])
        if len(s) >= 2 and int(s[:2]) <= 26:
            dfs(s[2:])

    dfs(s)
    return count

# extremely inefficient, exponential time complexity, so let's memoize our results
# also I just realized we don't need to splice the string each time, just adds complexity
# let's just keep track of the current index

def main(self, s: str) -> int:
    
    memo = {}
    def dfs(i):
        if i == len(s):
            return 1
        if s[i] == '0':
            return 0
        if i in memo:
            return memo[i]
        
        count = dfs(i + 1)
        if i + 1 < len(s) and int(s[i: i + 2]) <= 26:
            count += dfs(i + 2)

        memo[i] = count
        return count
    
    return dfs(0)


# we'll replace the memo with a dp array, going from beginning to end
#   otherwise it's the same, starting 0 is invalid, and check if double numbers are valid
def bottom_up(self, s: str) -> int:

    dp = [0] * (len(s) + 1)
    dp[len(s)] = 1

    for i in range(len(s) - 1, -1, -1):
        if s[i] == '0':
            dp[i] = 0
        else:
            dp[i] = dp[i + 1]
            if i + 1 < len(s) and int(s[i: i + 2]) <= 26:
                dp[i] += dp[i + 2]

    return dp[0]





if __name__ == "__main__":
    main()
