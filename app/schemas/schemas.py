from pydantic import BaseModel


class UserRequest(BaseModel):
    message: str


class AnalyzeResponse(BaseModel):
    status: str
    response: str
