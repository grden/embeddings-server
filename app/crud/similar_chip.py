from app.models.similar_chip import SimilarChipRequest, SimilarChipResponse
from app.core.openai_client import get_embeddings
from fastapi import HTTPException, status
import numpy as np

async def find_similar_chip(
    payload: SimilarChipRequest
) -> SimilarChipResponse:
    if not payload.available_chip_texts:
        return SimilarChipResponse(best_match_text=None)

    try:
        texts = [payload.preferred_chip_text] + payload.available_chip_texts
        embeddings = await get_embeddings(texts)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="The similarity service is temporarily unavailable."
        )

    preferred_vec = np.array(embeddings[0])
    available_vecs = [np.array(vec) for vec in embeddings[1:]]

    def cosine_similarity(a, b):
        return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

    similarities = [cosine_similarity(preferred_vec, vec) for vec in available_vecs]
    best_idx = int(np.argmax(similarities))

    # best_score = similarities[best_idx]

    # if best_score < SIMILARITY_THRESHOLD:
    #     return SimilarChipResponse(best_match_text=None)

    print(payload.available_chip_texts[best_idx])

    return SimilarChipResponse(best_match_text=payload.available_chip_texts[best_idx]) 