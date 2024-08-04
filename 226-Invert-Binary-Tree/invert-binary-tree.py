# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        #Base Case
        if not root:
            return None
        
        #Switch the right node with left node
        root.right, root.left = root.left, root.right

        #Recursively call right node and left node
        self.invertTree(root.right)
        self.invertTree(root.left)

        return root

        #Time Complexity: O(n) where n is the number of nodes. we visit each node once.
        #Space Complexity: O(h) where h is the height of the tree