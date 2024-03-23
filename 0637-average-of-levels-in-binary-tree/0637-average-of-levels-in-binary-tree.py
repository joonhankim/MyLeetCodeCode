# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        
        queue = [root]
        
        answer_list = []
        
        while queue:
            level_sum = 0
            level_nodes = len(queue)
            copied_level_nodes = level_nodes

            while copied_level_nodes:
                node = queue.pop(0)
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)   
                copied_level_nodes -= 1   
            answer_list.append(level_sum/level_nodes)
        return answer_list
            
        