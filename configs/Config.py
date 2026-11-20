from pydantic import BaseModel, Field


class Config(BaseModel):
    version: int
    experiment_name: str
    
