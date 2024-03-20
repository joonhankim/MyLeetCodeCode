# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.total = 0
        
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return
        #오른쪽 자식 노드 탐색
        self.convertBST(root.right)
        #합 갱신
        self.total += root.val
        # root.val을 합으로 갱신
        root.val = self.total
        #왼쪽 자식 노드 탐색
        self.convertBST(root.left)
            
        return root