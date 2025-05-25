# 567. Permutation In String
# Difficulty: Medium

# Link: https://leetcode.com/problems/permutation-in-string/description/

# doesn't look too bad
# initial thought: let's make a set from s1 and an occurrence array,
# then if a letter appears in s2 that occurs in s1, we keep iterating and subtracting from the array.
# if a letter didn't exist, or went below zero, we iterate again, starting after the letter we stopped at
# we also need to reset the array after each instance, but we can just copy again from a base template
# looked at the hints for a more elegant solution, we can just slide a window and update occurrences of current window
# vs what we're looking for, don't need letters set, count, etc., much simpler to implement
# time complexity: O(n)
# space complexity: O(1), forgot the arrs were constant size
# 40 minutes to solve

def solution(s1: str, s2: str) -> bool:

    if len(s1) > len(s2):
        return False

    occurrences = [0] * 26
    for c in s1:
        occurrences[ord(c) - ord('a')] += 1

    window = [0] * 26
    l = 0
    for r in range(len(s2)):
        char = s2[r]
        window[ord(char) - ord('a')] += 1

        if r - l + 1 == len(s1):
            if window == occurrences:
                return True
            l_char = s2[l]
            window[ord(l_char) - ord('a')] -= 1
            l += 1
    return False


# scrapping for now, backbone is right but it's so inelegant
# idea was to check at each occurrence of a letter in s1,
# slide until we matched all chars, else continue past the last comparison

# so many variables and stuff
# if len(s1) > len(s2):
#         return False

#     letters1 = set(s1)
#     count = len(s1)
#     occurrences = [0] * 26
#     for c in s1:
#         occurrences[ord(c) - ord('a')] += 1

#     i = 0
#     letters_copy = occurrences.copy()
#     while i < len(s2):
#         char = s2[i]
#         if char in letters1:
#             keep_going = True
#             while keep_going:
#                 char = s2[i]
#                 letters_copy[ord(char) - ord('a')] -= 1
#                 count -= 1

#                 if letters_copy[ord(char) - ord('a')] < 0:
#                     letters_copy = occurrences.copy()
#                     count = len(s1)
#                     keep_going = False
#                 if count == 0:
#                     return True
#                 i += 1

#         i += 1
#     return False





def main():
    s1 = "ab"
    s2 = "eidbaooo"#true
    print(solution(s1,s2))

    s1 = "ab"
    s2 = "eidboaoo"#false
    print(solution(s1,s2))

if __name__ == "__main__":
    main()
