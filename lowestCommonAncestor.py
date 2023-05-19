class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (p.left == q or p.right == q):
            return p

        if (q.left == p or q.right == p):
            return q 

        if (p.val <= root.val and q.val >= root.val) or (p.val >= root.val and q.val <= root.val): 
            return root
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)

s = Solution()
ex1 = TreeNode(6)
ex1.left = TreeNode(2)
ex1.right = TreeNode(8)
ex1.left.left = TreeNode(0)
ex1.left.right = TreeNode(4)
ex1.left.right.left = TreeNode(3)
ex1.left.right.right = TreeNode(5)
ex1.right.left = TreeNode(7)
ex1.right.right = TreeNode(9)
assert s.lowestCommonAncestor(ex1, ex1.left, ex1.right) == ex1
assert s.lowestCommonAncestor(ex1, ex1.left, ex1.left.right) == ex1.left
