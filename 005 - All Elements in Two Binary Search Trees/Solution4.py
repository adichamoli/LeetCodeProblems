'''48 / 48 test cases passed.                         Status: Accepted
Runtime: 420 ms                                       Memory Usage: 17.9 MB'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        def InOrder(root):
            if not root:
                return [] 
            stack,L=[],[]
            while True:
                while root:
                    stack.append(root)  
                    root=root.left
                    
                if stack:
                    node=stack.pop()
                else:
                    break
                L.append(node.val) 
                root=node.right
				
            return L    
            
        l1=InOrder(root1)
        l2=InOrder(root2)
        
        return sorted(l1+l2)
        