"""
============================================================
  11. TREES — LeetCode Style Exercises
============================================================
"""

from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ============================================================
# 1. Maximum Depth of Binary Tree (Easy)
# ============================================================
class Solution1:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        pass


# ============================================================
# 2. Invert Binary Tree (Easy)
# ============================================================
class Solution2:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        pass


# ============================================================
# 3. Same Tree (Easy)
# ============================================================
class Solution3:
    def isSameTree(self, p: Optional[TreeNode],
                   q: Optional[TreeNode]) -> bool:
        pass


# ============================================================
# 4. Symmetric Tree (Easy)
# ============================================================
class Solution4:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        pass


# ============================================================
# 5. Binary Tree Level Order Traversal (Medium)
# ============================================================
class Solution5:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass


# ============================================================
# 6. Validate Binary Search Tree (Medium)
# ============================================================
class Solution6:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        pass


# ============================================================
# 7. Lowest Common Ancestor of BST (Medium)
# ============================================================
class Solution7:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode,
                             q: TreeNode) -> TreeNode:
        pass


# ============================================================
# 8. Binary Tree Paths (Easy)
# ============================================================
class Solution8:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        pass


# ============================================================
# 9. Construct Binary Tree from Preorder and Inorder (Medium)
# ============================================================
class Solution9:
    def buildTree(self, preorder: List[int],
                  inorder: List[int]) -> Optional[TreeNode]:
        pass


# ============================================================
# 10. Serialize and Deserialize Binary Tree (Hard)
# ============================================================
class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        pass

    def deserialize(self, data: str) -> Optional[TreeNode]:
        pass
