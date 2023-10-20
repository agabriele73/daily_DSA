# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = deque()
        queue.append(root)
        output = []

        while queue:
            queueLen = len(queue)
            level = []

            for i in range(queueLen):
                # shift out from queue
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    # adding children to queue
                    queue.append(node.left)
                    queue.append(node.right)

            if level:
                output.append(level)

        return output


        