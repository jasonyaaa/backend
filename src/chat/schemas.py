from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class ChatMessageCreate(BaseModel):
    sender_id: str
    receiver_id: str
    content: str

class ChatMessageResponse(BaseModel):
    message_id: str
    sender_id: str
    receiver_id: str
    content: str
    created_at: datetime

class ChatHistoryResponse(BaseModel):
    messages: List[ChatMessageResponse]
