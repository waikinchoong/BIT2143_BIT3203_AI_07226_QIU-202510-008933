"""
Week 4 Lab — Implement Uninformed Search (BFS, DFS, UCS)

Complete remove_by_strategy() to implement:
- BFS (FIFO)
- DFS (LIFO)
- UCS (lowest cost)

Run:
    python3 lab.py

Test:
    python3 test_lab.py
"""


# ---------------------------------------------------------------------------
# Graph from class
# A is start, G is goal
# ---------------------------------------------------------------------------

GRAPH = {
    "A": [("B", 2), ("C", 5)],
    "B": [("D", 2), ("E", 4)],
    "C": [("F", 1)],
    "D": [("G", 5)],
    "E": [("G", 1)],
    "F": [("G", 1)],
    "G": [],
}


class Node:
    """A search-tree node."""

    def __init__(self, state, parent=None, cost=0):
        self.state = state
        self.parent = parent
        self.cost = cost

    def path(self):
        """Return path from start to this node."""
        node = self
        states = []

        while node is not None:
            states.append(node.state)
            node = node.parent

        return list(reversed(states))

    def __repr__(self):
        return f"Node({self.state!r}, cost={self.cost})"



def remove_by_strategy(frontier, strategy):
    """
    Remove and return ONE Node from frontier.

    BFS: First In First Out
    DFS: Last In First Out
    UCS: Lowest cost
    """

    if strategy == "bfs":
        # Remove oldest node
        return frontier.pop(0)

    elif strategy == "dfs":
        # Remove newest node
        return frontier.pop()

    elif strategy == "ucs":
        # Remove node with lowest cost
        min_index = min(
            range(len(frontier)),
            key=lambda i: frontier[i].cost
        )

        return frontier.pop(min_index)

    else:
        raise ValueError(f"Unknown strategy: {strategy!r}")



def search(graph, start, goal, strategy):
    """
    Generic search algorithm.
    """

    frontier = [Node(start, None, 0)]
    explored = set()
    expansion_order = []

    while frontier:

        node = remove_by_strategy(frontier, strategy)

        expansion_order.append(node.state)

        if node.state == goal:
            return node.path(), node.cost, expansion_order


        if node.state in explored:
            continue

        explored.add(node.state)


        for child_state, edge_cost in graph[node.state]:

            if child_state not in explored:

                frontier.append(
                    Node(
                        child_state,
                        node,
                        node.cost + edge_cost
                    )
                )


    return None, None, expansion_order



if __name__ == "__main__":

    for strat in ["bfs", "dfs", "ucs"]:

        path, cost, order = search(
            GRAPH,
            "A",
            "G",
            strat
        )

        print(f"{strat.upper():4s} | expansion order: {order}")
        print(f"       path: {path}  cost: {cost}\n")