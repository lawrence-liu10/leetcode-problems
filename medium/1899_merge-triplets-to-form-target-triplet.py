# 1899. Merge Triplets To Form Target Triplet
# Difficulty: Medium

# Link: https://leetcode.com/problems/merge-triplets-to-form-target-triplet/description/

# there's a couple checks we need to make
#   each number in the triplet must be less than or equal to the target's numbers (or we can't use it)
#       if it is, then it's a potentially valid merge
#       we then check if it's nums are equal to the targets, and at the end return based on if we found all 3 in our
#       potential candidates
def solution(self, triplets: list[list[int]], target: list[int]) -> bool:
    a_found = b_found = c_found = False
    for trip in triplets:
        if trip[0] > target[0] or trip[1] > target[1] or trip[2] > target[2]:
            continue

        if trip[0] == target[0]:
            a_found = True
        if trip[1] == target[1]:
            b_found = True
        if trip[2] == target[2]:
            c_found = True

        if a_found and b_found and c_found:
            return True
    return False




def main():
    pass

if __name__ == "__main__":
    main()
