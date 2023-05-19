class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root):
        inorder = self.inorder(root)
        for i in range(1, len(inorder)):
            if inorder[i] <= inorder[i-1]:
                return False
        return True

    def inorder(self, root):
        if not root:
            return []
        
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)

    def isValidBST2(self, root):
        stack, prev = [], -math.inf
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right
        return True
