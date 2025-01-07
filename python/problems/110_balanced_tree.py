# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def abs(x):
    return x if x >= 0 else -x

def depth(root):
    if root:
        return 1 + max(depth(root.left), depth(root.right))
    else:
        return 0


def isBalanced(root):
    return not root or isBalanced(root.left) and isBalanced(root.right) and abs(depth(root.left) - depth(root.right)) <= 1


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return isBalanced(root)
        