# Copyright (c) 2026 Debashis Bhattacharjee. All Rights Reserved.
# Unauthorized copying, modification, or distribution is prohibited.
# https://github.com/Debashis2007

"""Developer API Moderation — thin self-contained FastAPI POC."""

from __future__ import annotations

from typing import Optional

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, Field

from poc_core import MockLLM, TokenBucket, health_payload
from poc_core.safety import SafetyPlane
from poc_core.stores import InMemoryStore, MockVectorIndex

USE_CASE = "Developer API Moderation"
app = FastAPI(title=USE_CASE)
llm = MockLLM()
store = InMemoryStore()
safety = SafetyPlane()

@app.get("/health")
def health():
    return health_payload(USE_CASE)


class ChatIn(BaseModel):
    prompt: str

@app.post("/v1/chat")
async def chat(body: ChatIn):
    d = safety.check_input(body.prompt)
    if d.action != "allow":
        raise HTTPException(
            400,
            detail={"error": "safety_violation", "reason_code": d.reason_code, "policy_version": "2026-04"},
        )
    text = await llm.complete(body.prompt, max_tokens=12)
    return {"text": text, "policy_version": "2026-04"}
