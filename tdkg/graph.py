# tdkg/graph.py
import time
from typing import Dict, List
from .node import Node

class TimeDecayGraph:
    def __init__(self, decay_lambda: float = 0.001):
        self.nodes: Dict[str, Node] = {}
        self.decay_lambda = decay_lambda

    def add(self, content: str):
        # Dedup: simple exact match
        for node in self.nodes.values():
            if node.content == content:
                node.reinforce()
                return node.id

        node = Node(content)
        self.nodes[node.id] = node
        return node.id

    def query(self, text: str, top_k: int = 5) -> List[Node]:
        # naive keyword match scoring
        results = []
        for node in self.nodes.values():
            if text.lower() in node.content.lower():
                node.reinforce()
                results.append(node)

        results.sort(key=lambda x: x.importance, reverse=True)
        return results[:top_k]

    def decay(self):
        now = time.time()
        for node in self.nodes.values():
            node.decay(now, self.decay_lambda)

    def get_top_k(self, k: int = 5) -> List[Node]:
        return sorted(self.nodes.values(), key=lambda x: x.importance, reverse=True)[:k]

    def prune(self, threshold: float = 0.1):
        to_delete = [nid for nid, node in self.nodes.items() if node.importance < threshold]
        for nid in to_delete:
            del self.nodes[nid]