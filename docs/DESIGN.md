# Design: Developer API Moderation

**Project:** `developer-api-moderation`  
**Parent system design:** `06-safety-moderation-pipeline.md / 09`

## 1. What this POC demonstrates

API returns typed safety errors with policy version — never silent drops.

## 2. Architecture (POC)

```text
POST /v1/chat → safety → 400 safety_violation | completion
```

## 3. Patterns used (and why)

| Pattern | Why used | Where in code |
|---------|----------|---------------|
| Typed safety errors | Developers must handle violations in UX. | HTTP 400 detail object. |
| Policy version stamp | Debuggability when policy changes. | `policy_version`. |
| Shared decision plane idea | API and consumer should not diverge silently. | Same `SafetyPlane`. |

## 4. Key endpoints

`GET /health`, `POST /v1/chat`

## 5. Tradeoffs / POC limits

No SSE mid-stream safety event in this thin route.

## 6. How to run

See the **Run (self-contained POC)** section in [`../README.md`](../README.md).

This folder is self-contained and can be published as its own GitHub repository.

## 7. Design walkthrough video

> **Watch on YouTube:** [Developer Api Moderation — System Design #Shorts](https://youtu.be/qOXpDMFDfDc)
>
> Direct link: **https://youtu.be/qOXpDMFDfDc**

Also available in-repo:
- GIF preview: [`video/design-overview.gif`](./video/design-overview.gif)
- MP4 download: [`video/design-overview.mp4`](./video/design-overview.mp4)
- Narration script: [`video/narration.txt`](./video/narration.txt)

---

**Copyright (c) 2026 Debashis Bhattacharjee. All Rights Reserved.**  
Unauthorized copying or redistribution of this material is prohibited.  
GitHub: [Debashis2007](https://github.com/Debashis2007)

