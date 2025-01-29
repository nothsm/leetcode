"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        else:
            adj = {}
            visited = set()
            def visit(node):
                if node not in visited:
                    visited.add(node)
                    if node.val not in adj:
                        adj[node.val] = Node(node.val)
                    for v in node.neighbors:
                        if v.val not in adj:
                            adj[v.val] = Node(v.val)
                        nb = adj[v.val]
                        adj[node.val].neighbors.append(nb)
                        visit(v)
            visit(node)
            return adj[node.val]