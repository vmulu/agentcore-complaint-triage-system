# data modals for what the agent can accept

from typing import Literal
from pydantic import BaseModel, Field

class InvokePayload(BaseModel):
    subject: str = Field(min_length=1, max_length=200)
    redacted_body: str = Field(min_length=1, max_length=10_000)
    channel: Literal["email", "web_form", "mail"]
    sentiment: str | None = None
    priority: str
    account_mismatch: bool = False
    previous_draft: str | None = None
    staff_comment: str | None = Field(default=None, max_length=2_000)