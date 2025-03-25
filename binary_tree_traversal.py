def inorder(node):
    if node is None:
        return
    inorder(node.lptr)
    print(node.data, end=" ")
    inorder(node.rptr)

def preorder(node):
    if node is None:
        return
    print(node.data, end=" ")
    preorder(node.lptr)
    preorder(node.rptr)

def postorder(node):
    if node is None:
        return
    postorder(node.lptr)
    postorder(node.rptr)
    print(node.data, end=" ")
  
