import datetime
from enum import Enum
from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel
import uuid

class SpeakerRole(str, Enum):
    SELF = "self"      # 自己
    OTHER = "other"    # 對方

class Situation(SQLModel, table=True):
    """情境表"""
    __tablename__ = "situations"

    situation_id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    situation_name: str = Field(index=True)
    description: Optional[str] = None
    location: Optional[str] = None
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.now)

    # Relationships
    chapters: List["Chapter"] = Relationship(back_populates="situation")

class Chapter(SQLModel, table=True):
    """章節表"""
    __tablename__ = "chapters"

    chapter_id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    situation_id: uuid.UUID = Field(foreign_key="situations.situation_id")
    chapter_name: str = Field(index=True)
    description: Optional[str] = None
    sequence_number: int
    video_url: Optional[str] = None
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.now)

    # Relationships
    situation: Situation = Relationship(back_populates="chapters")
    sentences: List["Sentence"] = Relationship(back_populates="chapter")
    # 注意：為避免循環導入問題，暫時移除與 PracticeSession 的 Relationship
    # practice_sessions: List["PracticeSession"] = Relationship(back_populates="chapter")

class Sentence(SQLModel, table=True):
    """語句表"""
    __tablename__ = "sentences"

    sentence_id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    chapter_id: uuid.UUID = Field(foreign_key="chapters.chapter_id")
    sentence_name: str = Field(index=True)
    speaker_role: SpeakerRole
    role_description: Optional[str] = None
    content: str
    start_time: Optional[float] = None  # 在影片中的開始時間（秒）
    end_time: Optional[float] = None    # 在影片中的結束時間（秒）
    
    # 範例音訊檔案資訊（Optional）
    example_audio_path: Optional[str] = None
    example_audio_duration: Optional[float] = None  # 音訊時長（秒）
    example_file_size: Optional[int] = None         # 檔案大小（bytes）
    example_content_type: Optional[str] = None      # 檔案類型
    
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.now)

    # Relationships
    chapter: Chapter = Relationship(back_populates="sentences")
    # 注意：為避免循環導入問題，暫時移除與 PracticeRecord 的 Relationship
    # practice_records: List["PracticeRecord"] = Relationship(back_populates="sentence")

