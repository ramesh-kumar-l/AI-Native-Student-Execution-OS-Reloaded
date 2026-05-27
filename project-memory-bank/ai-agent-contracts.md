# AI Agent Contracts

## Overview
The AI-Native Student Execution OS uses autonomous execution agents (Planner, Revision, Accountability, Focus, Career, Reflection). Agents interact through structured data payloads rather than natural language messages to ensure reliability.

## Communication Interface
- Every agent request has a strict JSON structure.
- Responses must conform to structured schemas validated via Pydantic on the backend.

### Request Payload
```json
{
  "agent_name": "PlannerAgent",
  "task": "prioritize_schedule",
  "context": {
    "student_id": "uuid-v4",
    "tasks": [...],
    "schedule": [...]
  }
}
```

### Response Payload
```json
{
  "status": "success",
  "data": {
    "recommendations": [...]
  },
  "raw_cost_tokens": 1204
}
```

This contract isolates agent internals, allowing us to swap underlying model versions (e.g. Gemini 2.0 to 2.5) without breaking orchestration.
