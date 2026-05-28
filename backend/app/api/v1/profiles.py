import uuid
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.dependencies import get_db, get_current_user
from app.models.user import User
from app.api.schemas.profile import StudentProfileCreate, StudentProfileUpdate, StudentProfileResponse
from app.repositories.profile_repository import ProfileRepository

router = APIRouter(prefix="/profiles", tags=["Profiles"])
profile_repo = ProfileRepository()

@router.get("/me", response_model=StudentProfileResponse)
async def get_my_profile(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    profile = await profile_repo.get_by_user_id(db, current_user.id)
    if not profile:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Profile not found")
    return profile

@router.post("/", response_model=StudentProfileResponse)
async def create_profile(
    data: StudentProfileCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    existing = await profile_repo.get_by_user_id(db, current_user.id)
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Profile already exists")
    return await profile_repo.create(db, current_user.id, data)

@router.put("/me", response_model=StudentProfileResponse)
async def update_my_profile(
    data: StudentProfileUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    profile = await profile_repo.get_by_user_id(db, current_user.id)
    if not profile:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Profile not found")
    return await profile_repo.update(db, profile, data)
