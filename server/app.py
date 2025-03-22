from fastapi import FastAPI, HTTPException
from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

app = FastAPI()

# Charger les variables d'environnement (assure-toi d'avoir un fichier .env avec YOUTUBE_API_KEY)
load_dotenv()
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
if not YOUTUBE_API_KEY:
    raise Exception("La clé API YouTube n'est pas définie !")

@app.get("/youtube/channel-info/{query}")
async def get_channel_info_by_query(query: str):
    try:
        # Initialisation du client YouTube
        youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)
        
        # Recherche par nom pour obtenir l'ID de la chaîne
        search_response = youtube.search().list(
            part="snippet",
            q=query,
            type="channel",
            maxResults=1
        ).execute()
        
        # Vérifier si un résultat a été trouvé
        items = search_response.get("items")
        if not items:
            raise HTTPException(status_code=404, detail="Aucune chaîne trouvée pour cette recherche")
        
        # Récupérer l'ID de la chaîne
        channel_id = items[0]["id"]["channelId"]
        
        # Récupérer les informations détaillées de la chaîne (snippet et statistiques)
        channel_response = youtube.channels().list(
            part="snippet,statistics",
            id=channel_id
        ).execute()
        
        return channel_response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
