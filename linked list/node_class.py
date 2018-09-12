class Node:
    def __init__(self, val, next=None):
        self.next = next
        self.val = val

    @staticmethod
    def test_list():
        v = Node(6)
        c = Node(5, v)
        z = Node(4, c)
        y = Node(3, z)
        x = Node(2, y)
        head = Node(1, x)
        return head

    @staticmethod
    def print_list(z):
        while z:
            print(z.val)
            z = z.next