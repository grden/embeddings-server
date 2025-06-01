from fastapi import APIRouter, status, Depends
from app.models.similar_chip import SimilarChipRequest, SimilarChipResponse
from app.crud.similar_chip import find_similar_chip

router = APIRouter()

@router.post(
    "/find-similar",
    response_model=SimilarChipResponse,
    status_code=status.HTTP_200_OK,
    summary="Find the most similar chip text"
)
async def find_similar(
    payload: SimilarChipRequest
) -> SimilarChipResponse:
    return await find_similar_chip(payload) 