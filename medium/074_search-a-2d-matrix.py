# 074. Search A 2D Matrix
# Difficulty: Medium

# Link: https://leetcode.com/problems/search-a-2d-matrix/description/

# in c, 2d arrays are really just 1d, but I don't think that's the case for python
# We can remove a row at each step, but if each row only has one item that's O(m*n)
# We can actually run binary search m times, but that's still O(mlog(n))
# How do we use the second property
# idea: run binary search on the first cols, then do it on the remaining row

# implementation took me a while, I had to think about how to bin search cols
# need to compare with first element and last element in cur row
# also need to consider that our target might not be in the arrs,
# figuring these out was difficult
# time to solve: 45 min
# time complexity: O(log(n * m))
# space complexity: O(1)

def solution(matrix: list[list[int]], target: int) -> bool:

    rowU = 0
    rowD = len(matrix) - 1
    while rowU <= rowD:
        mid = (rowU + rowD) // 2
        if matrix[mid][0] > target:
            rowD = mid - 1
        elif matrix[mid][-1] < target:
            rowU = mid + 1
        else:
            break

    if not rowU <= rowD:
        return False

    row = (rowU + rowD) // 2
    l = 0
    r = len(matrix[0]) - 1
    while l <= r:
        mid = (l + r) // 2
        if matrix[row][mid] < target:
            l = mid + 1
        elif matrix[row][mid] > target:
            r = mid - 1
        else:
            return True
    return False


def main():
    pass

if __name__ == "__main__":
    main()
