class node1:
    def __init__(self, data):
        self.data = data
        self.lptr = None
        self.rptr = None

def insertion(root, ptr):
    while True:
        if ptr.data < root.data:
            if root.lptr is None:
                root.lptr = ptr
                break
            else:
                root = root.lptr
        else:
            if root.rptr is None:
                root.rptr = ptr
                break
            else:
                root = root.rptr



data = int(input("Enter the root node data: "))
list1 = [2, 4, 3, 4, 56, 3, 23, 54, 2, 3, 54, 23, 98, 23]

node = node1(data)
for i in list1:
    ptr = node1(i)
    insertion(node, ptr)

