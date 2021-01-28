'''63 / 63 test cases passed.                     Status: Accepted
Runtime: 36 ms                                    Memory Usage: 14.7 MB'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        if not root: return -1
        partialSum = 0
        return self.calcSum(root,partialSum)
    
    def calcSum(self,root,partialSum):
        if not root: return 0 #if tree has only one child (left or right)
        partialSum = partialSum * 2 + root.val #same as shiting left bit
        
        if not root.left and not root.right:
            return partialSum
        
        leftSum = self.calcSum(root.left,partialSum)
        rightSum = self.calcSum(root.right,partialSum)
        return leftSum + rightSum
        