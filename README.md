# Use Case: Developer API Moderation

**Author fingerprint:** `DBHATT-Debashis2007-SystemDesignPOC-2026` — Debashis Bhattacharjee ([@Debashis2007](https://github.com/Debashis2007))

**YouTube walkthrough:** [Developer Api Moderation — System Design #Shorts](https://youtu.be/qOXpDMFDfDc)

**Design doc:** [docs/DESIGN.md](./docs/DESIGN.md) — architecture, patterns, and why.


**Parent system design:** [06 — Multi-Layer Safety / Moderation](../06-safety-moderation-pipeline.md)  
**Also references:** [09 — API platform](../09-multi-model-routing-api-platform.md)

## Users & problem

API customers need predictable moderation behavior, machine-readable violations, and stable reason codes for their own UX—not opaque drops.

## Requirements & SLOs

| Requirement | Target |
|-------------|--------|
| Errors | Typed safety error + `reason_code` |
| Policy version | Returned / documented |
| Latency | Within API SLO budget |
| Audit | Per-request decision logs (policy-permitting) |

## Design (from parent)

```
API request → same Safety Decision Plane as consumer
  → allow | refuse | block
  → HTTP/SSE error events with codes
  → usage still metered fairly
```

Reuse unified policy plane from **06**; expose via **09** error taxonomy.

## Specializations

| Concern | API choice |
|---------|------------|
| Transparency | Document categories & codes |
| Streaming | Mid-stream safety event then terminate |
| Enterprise | Optional stricter packs |
| Abuse | Repeat offenders → key limits |

## Failure modes

- Silent 500 on safety block → never; return explicit safety error.
- Policy drift undocumented → version policies; changelog.
- Bypass via tools → tool outputs also moderated ([07](../07-agent-runtime-containment.md)).




## Design walkthrough (opens on GitHub)

> **Watch on YouTube:** [Developer Api Moderation — System Design #Shorts](https://youtu.be/qOXpDMFDfDc)


![Design overview](docs/video/design-overview.gif)

Full narrated video (download): [docs/video/design-overview.mp4](docs/video/design-overview.mp4)

## Run (self-contained POC)

This folder is a **standalone** project (safe to split into its own GitHub repo).

```bash
cd developer-api-moderation
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
PYTHONPATH=. python -m uvicorn app.main:app --reload --port 8000
```

```bash
curl -s http://127.0.0.1:8000/health | jq
```

curl -s -X POST http://127.0.0.1:8000/v1/chat -H 'Content-Type: application/json' -d '{"prompt":"jailbreak now"}' | jq

---

**Copyright (c) 2026 Debashis Bhattacharjee. All Rights Reserved.**  
Unauthorized copying or redistribution of this material is prohibited.  
GitHub: [Debashis2007](https://github.com/Debashis2007)

