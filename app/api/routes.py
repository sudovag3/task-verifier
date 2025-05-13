from fastapi import APIRouter, Depends, Header, HTTPException, status, Security
from fastapi.security import APIKeyHeader
from pydantic import BaseModel

from app.core.config import settings
from app.core.telegram_service import user_started_private_chat

router = APIRouter(prefix="", tags=["tasks"])

api_key_header = APIKeyHeader(name='Authorization')

class CompletionResponse(BaseModel, title="Task status"):
    completed: bool = True
@router.get(
    "/taskCompleted",
    response_model=CompletionResponse,
    summary="Check status of task",
)
async def task_completed(
    userId: int or str,
    taskId: str or None = None,
    api_key: str = Security(api_key_header),
) -> CompletionResponse:

    if api_key != settings.auth_token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    completed = await user_started_private_chat(userId)
    return CompletionResponse(completed=completed)


@router.get(
    "/userStatedBot",
    response_model=CompletionResponse,
    summary="Check status of task 2",
)
async def user_stated_bot(
    userId: int or str,
    userAddress: str or None = None,
    api_key: str = Security(api_key_header),
) -> CompletionResponse:

    if api_key != settings.auth_token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    completed = await user_started_private_chat(userId)
    return CompletionResponse(completed=completed)
