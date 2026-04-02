# tdkg/node.py
import time
import math
import uuid

class Node:
    def __init__(self, content: str):
        self.id = str(uuid.uuid4())
        self.content = content
        self.created_at = time.time()
        self.last_accessed = self.created_at
        self.access_count = 1
        self.importance = 1.0

    def reinforce(self):
        self.access_count += 1
        self.last_accessed = time.time()
        self.importance += 1.0

    def decay(self, now: float, decay_lambda: float):
        time_diff = now - self.last_accessed
        self.importance *= math.exp(-decay_lambda * time_diff)
    
    def __repr__(self):
        return f"Node(text='{self.text}', weight={self.weight:.2f})"