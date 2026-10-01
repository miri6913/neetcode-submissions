# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack = [[root, 1]]
        tmp = defaultdict(list)

        while stack:
            node, depth = stack.pop()

            if node:
                tmp[depth].append(node.val)

                left = [node.left, depth + 1]
                right = [node.right, depth + 1]

                stack.append(right)
                stack.append(left)

        return list(tmp.values())
        