from typing import Optional
from pydantic import BaseModel, Field


class UsuariLogin(BaseModel):
    id: int = Field(..., description="Unique identifier for the user")
    name: str = Field(..., description="User's display name")
    mail: str = Field(..., description="User's email address")
    hash: str = Field(..., description="Hashed password")

class CreateUsuariLogin(BaseModel):
    name: str = Field(..., description="User's display name (3-50 characters)")
    mail: str = Field(..., description="Valid email address")
    hash: str = Field(..., description="Password hash (minimum 8 characters)")

class AuthRequest(BaseModel):
    name: str = Field(..., description="User's display name (3-50 characters)")
    hash: str = Field(..., description="Password hash (minimum 8 characters)")

class UpdateUsuariName(BaseModel):
    name: str = Field(..., description="User's display name (3-50 characters)")

class UpdateUsuariMail(BaseModel):
    mail: str = Field(..., description="Valid email address")

class UpdateUsuariPassword(BaseModel):
    hash: str = Field(..., description="Password hash (minimum 8 characters)")

class Usuari(BaseModel):
    id: int = Field(..., description="Unique identifier for the user")
    name: str = Field(..., description="User's display name")
    mail: str = Field(..., description="User's email address")
    moxfield: str = Field(..., description="Moxfield link")
    archideckt: str = Field(..., description="Archideckt link")

class UpdateUsuari(BaseModel):
    name: Optional[str] = Field(None, description="User's display name (3-50 characters)")
    mail: Optional[str] = Field(None, description="Valid email address")
    moxfield: Optional[str] = Field(None, description="Moxfield link")
    archideckt: Optional[str] = Field(None, description="Archideckt link")

class SelectAllUsuari(BaseModel):
    pag: Optional[int] = Field(None,description="Offset")
    limit: Optional[int] = Field(None,description="Limit")
    name: Optional[str] = Field(None, description="User's display name (3-50 characters)")
    mail: Optional[str] = Field(None, description="Valid email address")
    moxfield: Optional[str] = Field(None, description="Moxfield link")
    archideckt: Optional[str] = Field(None, description="Archideckt link")