from sqlmodel import Session
from src.chat.models import ChatMessage

def save_message(session: Session, sender_id: str, receiver_id: str, content: str):
    message = ChatMessage(sender_id=sender_id, receiver_id=receiver_id, content=content)
    session.add(message)
    session.commit()
    session.refresh(message)
    return message

def get_chat_history(session: Session, user_id: str, other_user_id: str):
    return session.query(ChatMessage).filter(
        (ChatMessage.sender_id == user_id & ChatMessage.receiver_id == other_user_id) |
        (ChatMessage.sender_id == other_user_id & ChatMessage.receiver_id == user_id)
    ).order_by(ChatMessage.created_at).all()
