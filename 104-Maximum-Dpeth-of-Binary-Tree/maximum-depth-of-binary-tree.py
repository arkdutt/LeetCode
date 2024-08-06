# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        #Handling edge cases
        if not root:
            return 0
        
        #check the left child of root
        l = self.maxDepth(root.left)

        #check the right side of root
        r = self.maxDepth(root.right)
        maxx = max(l, r) + 1
        return maxx

        #Time Complexity: O(n) where n is the number of nodes
        #Space Complexity: O(H) where H is the height of the tree