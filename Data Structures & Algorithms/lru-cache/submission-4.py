class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.hsh = {} # val -> node
        self.dummy_head, self.dummy_tail = Node(), Node()
        self.dummy_head.nxt = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head
    
    def remove_node(self, node):
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev
        node.nxt, node.prev = None, None
        self.capacity += 1

    def append_node(self, node):
        prev = self.dummy_tail.prev
        prev.nxt = node
        self.dummy_tail.prev = node
        node.prev, node.nxt = prev, self.dummy_tail

        self.capacity -= 1
        self.check_remove_lru_node()
    
    def check_remove_lru_node(self):
        if self.capacity < 0:
            # remove most unused node
            to_remove = self.dummy_head.nxt
            self.remove_node(to_remove)
            del self.hsh[to_remove.key]

    def get(self, key: int) -> int:
        if key in self.hsh:
            # first, move to end of the linked list
            self.remove_node(self.hsh[key])
            self.append_node(self.hsh[key])
            return self.hsh[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hsh:
            self.hsh[key].val = value
            self.remove_node(self.hsh[key])
        else:
            self.hsh[key] = Node(value, key)
        self.append_node(self.hsh[key])
        

class Node:
    def __init__(self, val=0, key=0, nxt=None, prev=None):
        self.val = val
        self.key = key
        self.nxt = nxt
        self.prev = prev