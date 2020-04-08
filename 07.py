'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        def recursive(left, right):
            if left > right:
                return None
            root_val = preorder.pop()
            mid = inorder.index(root_val)
            root = TreeNode(root_val)
            root.left = recursive(left, mid - 1)
            root.right = recursive(mid + 1, right)
        
        return recursive(0, len(inorder) - 1)
'''

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        stack = []
        def recursive(left, right):
            if left > right:
                return None
            #print(left," ", right)
            root_val = stack.pop()
            #print(root_val)
            mid = inorder.index(root_val)
            #print(mid)
            root = TreeNode(root_val)
            root.left = recursive(left, mid - 1)
            root.right = recursive(mid + 1, right)
            return root
        while preorder:
            stack.append(preorder.pop())
        return recursive(0, len(inorder) - 1)

