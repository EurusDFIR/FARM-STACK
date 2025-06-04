from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right =None):
        self.val = val
        self.left = left
        self.right = right

        




def searchBST( root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
        return None
    if val ==root.val:
        return root
    elif val < root.val:
        return searchBST(root.left,val)
    else:
        root.right = searchBST(root.right,val)
def insert(root: Optional[TreeNode], val: int)->Optional[TreeNode]:
    if not root:
        return insert(root,val)



root = [4,2,7,1,3]
val = 2


