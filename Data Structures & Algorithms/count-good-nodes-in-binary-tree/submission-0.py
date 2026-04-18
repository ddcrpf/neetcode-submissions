# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def goodNodes(self, root: TreeNode) -> int:

        def traverse(node, max_val) -> int:
            if node is None:
                return 0
            cnt = 0
            if node.val >= max_val:
                cnt = 1

            max_val = max(max_val, node.val)
            leftcnt = traverse(node.left, max_val)
            rightcnt = traverse(node.right, max_val)

            cnt += leftcnt
            cnt += rightcnt

            return cnt
        return traverse(root, root.val)







# if Node is None:
#     return 0

# return 1 if node.val > maximum value else 0

# tree traverse 

# maximum value = max(node.val, maximum value)

        