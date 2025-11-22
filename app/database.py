import motor.motor_asyncio
from app.config import settings

_client = None
_db = None

async def connect_db():
  global _client, _db   # Set 'global' to modify the module-level variables declared at the top
  
  _client = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGO_URI)
  _db = _client[settings.DB_NAME]

async def close_db():
  _client.close()

def get_db():
  if _db is None:
    raise Exception("Database not connected yet.")
  return _db
