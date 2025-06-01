import httpx
from app.core.config import OPENAI_API_KEY

async def get_embeddings(texts: list[str]) -> list[list[float]]:
    url = "https://api.openai.com/v1/embeddings"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "text-embedding-3-small",
        "input": texts
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        return [item["embedding"] for item in data["data"]] 