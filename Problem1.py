# Using a queue approach, while q is not empty keep popping and adding the left and right until you reach the size of the queue and then add those to the result array
# TC: O(N)
# SC: O(N)
# Yes, this worked in leetcode


from queue import Queue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = Queue()
        q.put(root)
        while not q.empty():
            size = q.qsize()
            answer = []
            for i in range(size):
                curr = q.get()
                answer.append(curr.val)
                if curr.left:
                    q.put(curr.left)
                if curr.right:
                    q.put(curr.right)
            res.append(answer)
        return res
