'''48 / 48 test cases passed.                         Status: Accepted
Runtime: 308 ms                                       Memory Usage: 17.6 MB'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def treeToList(self, root: TreeNode) -> List[int]:
        stack = []
        lis = []
        current = root
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                lis.append(current.val)
                current = current.right
        return lis
        
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        list1 = self.treeToList(root1)
        list2 = self.treeToList(root2)
        list3 = list1+list2
        return(sorted(list3))
        