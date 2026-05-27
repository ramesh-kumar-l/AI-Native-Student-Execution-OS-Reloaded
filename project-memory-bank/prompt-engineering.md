# Prompt Engineering

## General Principles
- **System Instructions**: All system prompts must clearly state the LLM's role, constraints, input payload schemas, and target output structure.
- **Strict Formatting**: Force outputs into JSON structure using model parameters or Gemini schema constraints rather than regex text parsing.
- **Context Injection**: Minimize context token bloating by indexing documents (RAG) and feeding only top-N chunks instead of full files.
- **Traceability**: Save prompts and inputs with correlation IDs to evaluate performance and debug completions.
