class TreeNode:
    def __init__(self, val = 0,left = None, right =None):

        self.val  = val
        self.left = left
        self.right = right

def search_bst(root: TreeNode, target: int)->TreeNode:
    if not root:
        return None
    
    if target ==root.val:
        return root
    elif target < root.val:
        return search_bst(root.left,target)
    else:
        return search_bst(root.right, target)
    

def insert(root: TreeNode, val: int)->TreeNode:
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left,val)
    else:
        root.right = insert(root.right,val)
    return root

def inorder(root: TreeNode):
    if root:
        inorder(root.left)
        print(root.val,end =' ')
        inorder(root.right)


root = None
for v in [8,3,10,1,6]:
    root = insert(root,v)
inorder(root)
    