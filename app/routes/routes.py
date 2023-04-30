from fastapi import APIRouter
from app.actions import actions
from app.schemas import schemas


router = APIRouter(prefix='', tags=[''])


@router.get('/health-check')
async def health_check():
    return {'Status': 'Working'}


@router.get('/paraphrase')
async def paraphrase_sentence(tree: str, limit: int = 20):
    return actions.paraphrase(tree + ',', limit)
