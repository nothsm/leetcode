"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        old_to_new = dict()
        def dfs(node):
            if node in old_to_new:
              return old_to_new[node]
            cloned = Node(node.val)
            old_to_new[node] = cloned
            cloned.neighbors = [dfs(neighbor) for neighbor in node.neighbors]
            return cloned
        return dfs(node) if node else None
