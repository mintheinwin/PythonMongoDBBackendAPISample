from fastapi import APIRouter, Depends, HTTPException, status
from app.database import get_db
from app.models.user import UserCreate
from bson import ObjectId

router = APIRouter()

# Get a user by ObjectId
@router.get("/{user_id}")
async def get_user(user_id: str, db=Depends(get_db)):
  # If we don't need _id, just do '_id': 0
  user = await db.users.find_one({"_id": ObjectId(user_id)}, { '_id': 1, 'name': 1, 'userID': 1 })
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

  user["_id"] = str(user["_id"])
  return user

# Create a new user
from fastapi import HTTPException, status

@router.post("/")
async def create_user(user: UserCreate, db = Depends(get_db)):

    # Check if userID already exists
    existing_user = await db.users.find_one({"userID": user.userID})
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"userID '{user.userID}' already exists"
        )

    # Insert new user
    result = await db.users.insert_one(user.model_dump())

    return {
        "id": str(result.inserted_id),
        "userID": str(user.userID),
        "name": str(user.name)
    }

# Get a user by ObjectId
@router.get("/{user_id}")
async def get_user(user_id: str, db=Depends(get_db)):
  # If we don't need _id, just do '_id': 0
  user = await db.users.find_one({"_id": ObjectId(user_id)}, { '_id': 1, 'name': 1, 'userID': 1 })
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

  user["_id"] = str(user["_id"])
  return user


@router.get("/")
async def get_all_users(db = Depends(get_db)):
    users = []

    cursor = db.users.find({})   # find all documents
    async for user in cursor:
        user["_id"] = str(user["_id"])  # convert ObjectId to string
        users.append(user)

    return users


