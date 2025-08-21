import datetime
from typing import Optional
from sqlmodel import Field, SQLModel
import uuid

# Add a comment to clarify the purpose of the ChatMessage model
class ChatMessage(SQLModel, table=True):
    """聊天訊息表"""
    __tablename__ = "chat_messages"

    message_id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    sender_id: str = Field(index=True)
    receiver_id: str = Field(index=True)
    content: str
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
