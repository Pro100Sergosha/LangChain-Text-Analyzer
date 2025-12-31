from fastapi import Depends, APIRouter
from sqlmodel import Session

from app.db.database import get_session
from app.models.ai import MessageLog
from app.schemas.schemas import UserRequest, AnalyzeResponse
from app.services.ai_service import process_message_with_ai

router = APIRouter(tags=["analyzer"])


@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze_message(
    request: UserRequest,
    session: Session = Depends(get_session),
):
    user_text = request.message

    ai_response = await process_message_with_ai(user_text)

    db_entry = MessageLog(
        user_message=user_text,
        topic=ai_response.get("topic", "Unknown"),
        language=ai_response.get("language", "Unknown"),
        sentiment=ai_response.get("sentiment", "Unknown"),
        ai_response_text=ai_response.get("text", "No response generated"),
    )

    session.add(db_entry)
    session.commit()
    session.refresh(db_entry)

    return AnalyzeResponse(status="success", response=ai_response.get("text", ""))
