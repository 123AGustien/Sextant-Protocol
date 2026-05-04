# poc_demo.py – Cascade Lens V2 (RP-Enforced Minimal Simulator)

"""
Deterministic sandbox simulation engine with embedded RP constraints:
- RP-01: Infrastructure Diversity
- RP-02: Control Plane Independence
- RP-03: Cascade Containment
"""

import copy

# ----------------------------
# Core Simulation State
# ----------------------------

class Node:
    def __init__(self, node_id, health=1.0):
        self.id = node_id
        self.health = health
        self.connections = []

    def connect(self, other):
        self.connections.append(other)


# ----------------------------
# RP-01: Diversity Principle
# ----------------------------
# Ensures multiple dependency paths exist

def check_diversity(nodes):
    for node in nodes:
        if len(node.connections) < 1:
            print(f"[RP-01 WARNING] Node {node.id} has low diversity")


# ----------------------------
# RP-02: Control Independence
# ----------------------------
# Input events cannot directly mutate system state

def apply_event(node, severity):
    # event is processed, NOT directly injected
    return max(0.0, node.health - severity * 0.5)


# ----------------------------
# RP-03: Containment Principle
# ----------------------------
# Limits cascade propagation depth

MAX_DEPTH = 3


def cascade(node, severity, depth=0, visited=None):
    if visited is None:
        visited = set()

    if depth > MAX_DEPTH:
        return

    if node.id in visited:
        return

    visited.add(node.id)

    # Apply controlled degradation
    node.health = apply_event(node, severity)

    print(f"Node {node.id} health: {node.health:.2f}")

    # Propagate with reduced severity
    for child in node.connections:
        cascade(child, severity * 0.6, depth + 1, visited)


# ----------------------------
# Demo Execution
# ----------------------------

if __name__ == "__main__":

    # Create simple graph
    A = Node("A")
    B = Node("B")
    C = Node("C")

    A.connect(B)
    B.connect(C)

    nodes = [A, B, C]

    # RP-01 check
    check_diversity(nodes)

    print("\n--- Cascade Simulation Start ---\n")

    # Trigger failure at root node
    cascade(A, severity=0.8)
