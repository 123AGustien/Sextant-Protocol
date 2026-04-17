from core.cascade_engine import CascadeEngine

def simulate(request, engine):
    """
    Executes deterministic sandbox simulation.
    """

    events = request.get("events", [])
    results = []

    for event in events:
        result = engine.execute(event)
        results.append(result)

    return {
        "status": "success",
        "deterministic": True,
        "results": results
    }
  class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, key, value):
        self.nodes[key] = value

    def get(self, key):
        return self.nodes.get(key)


class CascadeEngine:
    def __init__(self, graph):
        self.graph = graph

    def execute(self, event):
        node = self.graph.get(event["node"])

        return self._propagate(node, event)

    def _propagate(self, node, event):
        return {
            "node": node,
            "event_type": event.get("type"),
            "status": "simulated"
        }
