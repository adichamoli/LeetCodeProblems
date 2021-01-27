'''48 / 48 test cases passed.                         Status: Accepted
Runtime: 548 ms                                       Memory Usage: 23 MB'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def traverse(node):
            if not node:
                return []
            return [node.val] + traverse(node.left) + traverse(node.right)
 
        res = traverse(root1)
        res += traverse(root2)
        return sorted(res)
        