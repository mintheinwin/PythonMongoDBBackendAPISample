from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
  # NOTE: The variable names here must match those defined in .env file
  MONGO_URI: str  # mongo_uri: str = Field(..., env="MONGO_URI")
  DB_NAME: str

  model_config = SettingsConfigDict(env_file='.env')

settings = Settings()
