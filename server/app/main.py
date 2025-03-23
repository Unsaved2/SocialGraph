from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware 
import json, os

app = FastAPI()

# Add CORS middleware to allow requests from your Next.js domain (adjust as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Change to your client's URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_graph_file_path():
    # Get the absolute path of the current file (this script)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # Adjust the relative path to point to the data directory
    # For example, if the structure is:
    #   project/
    #     ├── data/
    #     │    └── graphe.json
    #     └── app/
    #          └── main.py
    # then you need to go up one level from the app folder to reach data:
    path = os.path.join(base_dir, "..", "data", "graph.json")
    # Return the absolute path
    return os.path.abspath(path)

@app.get("/graph")
def get_graphe():
    chemin = get_graph_file_path()
    if not os.path.exists(chemin):
        raise HTTPException(status_code=404, detail="Graph non disponible. Veuillez déclencher le pré-calcul.")
    with open(chemin, "r", encoding="utf-8") as f:
        graph = json.load(f)
    return graph

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)