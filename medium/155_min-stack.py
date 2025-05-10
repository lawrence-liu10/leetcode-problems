# 155. Min Stack
# Difficulty: Medium

# Link: https://leetcode.com/problems/min-stack/description/

# push, pop, top, min element need to be constant time
# need an array at least to hold elements
# stack is lifo
# idea: keep a tail counter cur
# push, two cases: empty, then append, otherwise append and move cur one
# top returns arr[cur], pop moves cur back one
# for the minimum, can we make a min heap? amortized O(1)
# can we delete arbitrary elements in a min heap? not really

# thought for 20 min, about the heap and another sorted array before looking at hint
# we can implement two stacks, one only holds the min(prev vals, cur)
# push, pop, top simple
# min, we return pop of min stack

class MinStack:

    def __init__(self):
        self.arr = []
        self.min_stack = []



    def push(self, val: int) -> None:
        self.arr.append(val)

        # if not self.min_stack:
        #     self.min_stack.append(val)
        # elif val < self.min_stack[-1]:
        #     self.min_stack.append(val)
        # else:
        #     self.min_stack.append(self.min_stack[-1])
        # don't need all these if statements
        min_val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(min_val)


    def pop(self) -> None:
        self.arr.pop()
        self.min_stack.pop()


    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


def main():
    pass

if __name__ == "__main__":
    main()
