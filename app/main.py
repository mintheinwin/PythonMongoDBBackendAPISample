# Run by using the command below:
#     uvicorn main:app --reload

from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.database import connect_db, close_db
from app.routers import users

@asynccontextmanager
async def lifespan(app: FastAPI):
  # Upon startup, connect to DB
  await connect_db()
  print("\tConnected to DB!")
  yield   # Pause until the app shuts down
  
  # Upon shutdown, close connection to DB
  await close_db()
  print("\tDisconnected from DB!")

app = FastAPI(lifespan=lifespan)

# Include routers
app.include_router(users.router, prefix="/users", tags=["users"])   # 'tags' is for API documentation
# app.include_router(scenarios.router, prefix="/scenarios", tags=["scenarios"])
# app.include_router(files.router, prefix="/files", tags=["files"])
