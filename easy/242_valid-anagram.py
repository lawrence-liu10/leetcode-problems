# 242. Valid Anagram
# Difficulty: Easy

# Link: https://leetcode.com/problems/valid-anagram/description/


# Add the letters from one word to a hash map
# iterate using second word, subtracting letters
# Time: O(s + t)
# Space: O(1) (hashmap contains <= 26 keys)
def solution(s: str, t: str) -> bool:

    if len(s) != len(t):
        return False
    
    letters = {}
    for char in s:
        letters[char] = letters.get(char, 0) + 1
    
    for char in t:
        if char not in letters or letters[char] == 0:
            return False
        letters[char] -= 1

    return True


def main():

    s1 = "anagram"
    t1 = "nagaram"

    s2 = "rat"
    t2 = "car"


    print(solution(s1,t1))



if __name__ == "__main__":
    main()
