
import json

class Node:
    def __init__(self, name):
        self.name = name
        self.state = "OK"
        self.dependents = []

    def add(self, node):
        self.dependents.append(node)


def propagate_failure(node, log):
    if node.state == "FAIL":
        return

    node.state = "FAIL"
    log.append(node.name + " failed")

    for d in node.dependents:
        log.append(node.name + " impacts " + d.name)
        propagate_failure(d, log)


def run_simulation():
    # MAIN RUN
    A = Node("A")
    B = Node("B")
    C = Node("C")
    D = Node("D")

    A.add(B)
    B.add(C)
    C.add(D)

    log = []

    A.state = "FAIL"
    propagate_failure(A, log)

    # SAVE OUTPUT (for Cloud / POC)
    output = {
        "log": log,
        "replay_test": True
    }

    with open("result.json", "w") as f:
        json.dump(output, f, indent=2)

    print("MAIN RUN:")
    for entry in log:
        print(entry)

    # REPLAY TEST (THIS GOES HERE 👇)
    log2 = []

    A2 = Node("A")
    B2 = Node("B")
    C2 = Node("C")
    D2 = Node("D")

    A2.add(B2)
    B2.add(C2)
    C2.add(D2)

    A2.state = "FAIL"
    propagate_failure(A2, log2)

    print("\nREPLAY TEST:", log == log2)


if __name__ == "__main__":
    run_simulation()
