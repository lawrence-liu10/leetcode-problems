# 424. Longest Repeating Character Replacement
# Difficulty: Medium

# Link: https://leetcode.com/problems/longest-repeating-character-replacement/

# still sick and the knicks lost, rough night😔
# sliding window problem
# at first I was thinking we use a set to hold the letters, but probably a hashmap
# or arr is better, I think arr b/c 26 possible letters only
# in each window, we check len window minus most frequent letter, that gives us 
# the # of elements to replace, if it's <= k, it's the new max
# if it's > k, move left pointer until it isn't
# time to solve: 40 min
# time complexity: O(n)
# space complexity: O(1)
def solution(s: str, k: int) -> int:
    
    l = 0
    r = 0
    sol = 0
    freqs = [0] * 26
    while r < len(s):
        freqs[ord(s[r]) - ord('A')] += 1

        while (r - l + 1) - max(freqs) > k:
            freqs[ord(s[l]) - ord('A')] -= 1
            l += 1

        if r - l + 1 > sol:
            sol = r - l + 1
        r += 1
    return sol

def main():
    s = "ABAB"
    k = 2#4
    print(solution(s,k))

    s = "AABABBA"
    k = 1#4
    print(solution(s,k))
    
if __name__ == "__main__":
    main()
