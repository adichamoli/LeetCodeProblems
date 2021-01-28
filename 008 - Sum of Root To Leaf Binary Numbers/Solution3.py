'''63 / 63 test cases passed.                     Status: Accepted
Runtime: 72 ms                                    Memory Usage: 14.7 MB'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode):
        ret = []
        
        def recursive(root, prefix):
            if not root: return None
            
            if not root.left and not root.right:
                ret.append(prefix + str(root.val))
                return 
            if root.left: recursive(root.left, prefix + str(root.val))
            if root.right: recursive(root.right, prefix + str(root.val))

        recursive(root, '')        
        return sum([int(x, 2) for x in ret])
        