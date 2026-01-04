from pydantic import BaseModel


class UserRequest(BaseModel):
    """
    Schema representing a user's request containing a message.
    """
    message: str


class AnalyzeResponse(BaseModel):
    """
    Schema representing the response after analyzing a user's message.
    """
    status: str
    response: str
