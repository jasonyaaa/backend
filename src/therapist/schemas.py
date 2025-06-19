from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime

from src.auth.models import UserRole

class TherapistClientCreate(BaseModel):
    client_id: UUID

    class Config:
        json_schema_extra = {
            "example": {
                "client_id": "550e8400-e29b-41d4-a716-446655440002"
            }
        }

class TherapistClientResponse(BaseModel):
    id: UUID
    therapist_id: UUID
    client_id: UUID
    created_at: datetime
    
    # 包含用戶基本信息，便於前端直接使用
    client_info: Optional[Dict[str, Any]] = None
    therapist_info: Optional[Dict[str, Any]] = None

    class Config:
        json_schema_extra = {
            "example": {
                "id": "550e8400-e29b-41d4-a716-446655440003",
                "therapist_id": "550e8400-e29b-41d4-a716-446655440001",
                "client_id": "550e8400-e29b-41d4-a716-446655440002",
                "created_at": "2025-05-01T06:03:56.458985",
                "client_info": {
                    "name": "林小華",
                    "gender": "女",
                    "age": 30
                },
                "therapist_info": {
                    "name": "陳醫師",
                    "gender": "男"
                }
            }
        }

class TherapistClientListResponse(BaseModel):
    total: int
    therapist_clients: List[TherapistClientResponse]

    class Config:
        json_schema_extra = {
            "example": {
                "total": 1,
                "therapist_clients": [{
                    "id": "550e8400-e29b-41d4-a716-446655440003",
                    "therapist_id": "550e8400-e29b-41d4-a716-446655440001",
                    "client_id": "550e8400-e29b-41d4-a716-446655440002",
                    "created_at": "2025-05-01T06:03:56.458985",
                    "client_info": {
                        "name": "林小華",
                        "gender": "女",
                        "age": 30
                    },
                    "therapist_info": {
                        "name": "陳醫師",
                        "gender": "男"
                    }
                }]
            }
        }

# 治療師檔案相關 Schema
class TherapistProfileCreate(BaseModel):
    license_number: str = Field(..., min_length=5, max_length=50)
    specialization: Optional[str] = Field(None, max_length=200)
    bio: Optional[str] = Field(None, max_length=1000)
    years_experience: Optional[int] = Field(None, ge=0, le=50)
    education: Optional[str] = Field(None, max_length=500)
    
    class Config:
        json_schema_extra = {
            "example": {
                "license_number": "TH123456",
                "specialization": "語言治療",
                "bio": "專精於兒童語言發展治療，具有豐富的臨床經驗。",
                "years_experience": 5,
                "education": "國立陽明交通大學語言治療學系碩士"
            }
        }

class TherapistProfileUpdate(BaseModel):
    license_number: Optional[str] = Field(None, min_length=5, max_length=50)
    specialization: Optional[str] = Field(None, max_length=200)
    bio: Optional[str] = Field(None, max_length=1000)
    years_experience: Optional[int] = Field(None, ge=0, le=50)
    education: Optional[str] = Field(None, max_length=500)
    
    class Config:
        json_schema_extra = {
            "example": {
                "specialization": "兒童語言治療",
                "bio": "專精於兒童語言發展治療，具有豐富的臨床經驗。",
                "years_experience": 6
            }
        }

class TherapistProfileResponse(BaseModel):
    profile_id: UUID
    user_id: UUID
    license_number: str
    specialization: Optional[str]
    bio: Optional[str]
    years_experience: Optional[int]
    education: Optional[str]
    created_at: datetime
    updated_at: datetime
    
    class Config:
        json_schema_extra = {
            "example": {
                "profile_id": "550e8400-e29b-41d4-a716-446655440005",
                "user_id": "550e8400-e29b-41d4-a716-446655440001",
                "license_number": "TH123456",
                "specialization": "語言治療",
                "bio": "專精於兒童語言發展治療，具有豐富的臨床經驗。",
                "years_experience": 5,
                "education": "國立陽明交通大學語言治療學系碩士",
                "created_at": "2025-05-01T06:03:56.458985",
                "updated_at": "2025-05-01T06:03:56.459284"
            }
        }

# 增強的用戶回應 Schema，包含治療師檔案
class UserWithProfileResponse(BaseModel):
    user_id: UUID
    account_id: UUID
    name: str
    gender: Optional[str]
    age: Optional[int]
    phone: Optional[str]
    role: UserRole
    created_at: datetime
    updated_at: datetime
    therapist_profile: Optional[TherapistProfileResponse] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "user_id": "550e8400-e29b-41d4-a716-446655440001",
                "account_id": "550e8400-e29b-41d4-a716-446655440000",
                "name": "陳醫師",
                "gender": "男",
                "age": 35,
                "phone": "0912345678",
                "role": "therapist",
                "created_at": "2025-05-01T06:03:56.458985",
                "updated_at": "2025-05-01T06:03:56.459284",
                "therapist_profile": {
                    "profile_id": "550e8400-e29b-41d4-a716-446655440005",
                    "user_id": "550e8400-e29b-41d4-a716-446655440001",
                    "license_number": "TH123456",
                    "specialization": "語言治療",
                    "bio": "專精於兒童語言發展治療。",
                    "years_experience": 5,
                    "education": "國立陽明交通大學語言治療學系碩士",
                    "created_at": "2025-05-01T06:03:56.458985",
                    "updated_at": "2025-05-01T06:03:56.459284"
                }
            }
        }

# 治療師申請成為治療師的 Schema
class TherapistApplicationRequest(BaseModel):
    license_number: str = Field(..., min_length=5, max_length=50)
    specialization: str = Field(..., min_length=2, max_length=200)
    bio: str = Field(..., min_length=10, max_length=1000)
    years_experience: int = Field(..., ge=0, le=50)
    education: str = Field(..., min_length=5, max_length=500)
    
    class Config:
        json_schema_extra = {
            "example": {
                "license_number": "TH123456",
                "specialization": "語言治療",
                "bio": "專精於兒童語言發展治療，具有豐富的臨床經驗。",
                "years_experience": 5,
                "education": "國立陽明交通大學語言治療學系碩士"
            }
        }
