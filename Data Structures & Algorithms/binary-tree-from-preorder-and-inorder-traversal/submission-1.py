# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder or not inorder:
            return None

        inorder_map = {v:i for i,v in enumerate(inorder)}


        root_val = preorder[0]
        root = TreeNode(root_val)

        # mid_index = inorder.index(root_val)
        mid_index = inorder_map[root_val]


        root.left = self.buildTree(preorder[1:mid_index+1], inorder[:mid_index])
        root.right = self.buildTree(preorder[mid_index+1:], inorder[mid_index + 1:])

        return root

