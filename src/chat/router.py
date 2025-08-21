from fastapi import APIRouter, WebSocket, Depends
from sqlmodel import Session
from src.shared.database.database import get_session
from src.chat.services.chat_service import save_message, get_chat_history
from src.chat.schemas import ChatMessageCreate, ChatHistoryResponse

router = APIRouter(prefix="/chat", tags=["Chat"])

@router.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: str):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message from {user_id}: {data}")

@router.post("/send", response_model=ChatMessageCreate)
def send_message(
    message_data: ChatMessageCreate,
    session: Session = Depends(get_session)
):
    return save_message(session, message_data.sender_id, message_data.receiver_id, message_data.content)

@router.get("/history/{user_id}/{other_user_id}", response_model=ChatHistoryResponse)
def get_history(
    user_id: str,
    other_user_id: str,
    session: Session = Depends(get_session)
):
    messages = get_chat_history(session, user_id, other_user_id)
    return {"messages": messages}