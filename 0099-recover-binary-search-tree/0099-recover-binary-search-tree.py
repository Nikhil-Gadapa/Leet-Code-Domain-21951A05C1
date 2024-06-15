# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Initialize the pointers needed for finding the swapped nodes
        startnode = lastnode = prev = None

        # Define the in-order traversal function
        def dfs(root):
            nonlocal startnode, lastnode, prev
            if not root:
                return

            # Traverse the left subtree
            dfs(root.left)

            # Process the current node
            if prev and prev.val > root.val:
                if not startnode:
                    startnode = prev  # The first misplaced node
                lastnode = root  # The second misplaced node
            prev = root  # Update prev to the current node

            # Traverse the right subtree
            dfs(root.right)

        # Call the in-order traversal starting from the root
        dfs(root)

        # Swap the values of the two misplaced nodes
        if startnode and lastnode:
            startnode.val, lastnode.val = lastnode.val, startnode.val
