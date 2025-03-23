import json
import os

def calculate_graph():
    # Example of a simple structure for 500 people
    graph = {
        "nodes": [{"id": f"YT{i}", "label": f"YouTuber {i}"} for i in range(1, 501)],
        "edges": [{"from": f"YT{i}", "to": f"YT{j}"} for i in range(1, 501) for j in range(i+1, i+2)]
    }
    return graph

def save_graph(graph):
    # Get the absolute path of the folder where this script is located
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Build the path to "server/data/graph.json"
    # (if you have the "data" folder inside "server")
    path = os.path.join(base_dir, "..", "..", "data", "graph.json")

    # Create the data/ folder if it doesn't exist
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(graph, f, ensure_ascii=False, indent=2)
    print(f"Graph saved in {path}")

if __name__ == "__main__":
    graph = calculate_graph()
    save_graph(graph)
    print("Pre-calculation completed and graph saved.")
