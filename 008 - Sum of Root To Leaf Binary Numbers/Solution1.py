'''63 / 63 test cases passed.                     Status: Accepted
Runtime: 32 ms                                    Memory Usage: 14.7 MB'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def preorder(r, cur_number):
            nonlocal root_to_leaf
            if r:
                cur_number = (cur_number << 1) | r.val
                # if it's a leaf, update root-to-leaf sum
                if not (r.left or r.right):
                    root_to_leaf += cur_number
                    
                preorder(r.left, cur_number)
                preorder(r.right, cur_number) 
        
        root_to_leaf = 0
        preorder(root, 0)
        return root_to_leaf
        