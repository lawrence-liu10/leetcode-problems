# 146. Lru Cache
# Difficulty: Medium

# Link: https://leetcode.com/problems/lru-cache/

# doubly linked list question, we can make nodes with key val pairs while keeping a head and tail pointer
# each time we add a pair, we put it in a map storing key vals
# to keep it LRU, if a node is accessed/pushed, we move it to the front
# when n == capacity, we can move the tail and delete from the map

class LRUCache:
    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.next = None
            self.prev = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = self.Node(-1, -1)
        self.tail = self.Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}

    def push_front(self, node: Node):
        temp = self.head.next
        node.next = temp
        node.prev = self.head
        self.head.next = node
        temp.prev = node

    def del_node(self, node: Node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.del_node(node)
            self.push_front(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.del_node(node)
            self.push_front(node)
        else:
            if len(self.map) >= self.capacity:
                lru_node = self.tail.prev
                self.del_node(lru_node)
                del self.map[lru_node.key]
            new_node = self.Node(key, value)
            self.map[key] = new_node
            self.push_front(new_node)

def solution():
    pass

def main():
    pass

if __name__ == "__main__":
    main()
