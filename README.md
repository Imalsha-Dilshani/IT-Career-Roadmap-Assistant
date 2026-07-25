# IT Career Roadmap Assistant

## Project Description
AI-powered IT career guidance assistant using RAG, LLM, and multiple agents.

## Architecture Diagram

(User)
   |
   v
Streamlit UI
   |
   v
Agent System
   |
   +--> Career Agent
   |
   +--> Skill Agent
   |
   +--> Roadmap Agent
   |
   v
RAG Pipeline
   |
   +--> PDF Documents
   |
   +--> Chunking
   |
   +--> Embeddings
   |
   +--> FAISS Vector Database
   |
   v
LLM (Llama via OpenRouter)


## RAG Pipeline Explanation

1. Domain documents collected
2. PDF text extraction
3. Document chunking
4. Sentence-transformer embeddings
5. FAISS vector storage
6. Similarity search
7. Retrieved context sent to LLM


## Model Choice Comparison

| Model | Pros | Cons |
|---|---|---|
| Llama 3.3 70B | High quality reasoning | Larger model |
| GPT-4 | Strong performance | Paid API |
| Mistral | Fast | Lower reasoning ability |

Selected Model:
Llama 3.3 70B via OpenRouter


## Agent Communication Diagram


User
 |
Career Agent
 |
Skill Analysis Agent
 |
Roadmap Agent
 |
Final Response


## Streamlit Demo

(Add your deployed Streamlit URL)


## Known Limitations

- Depends on document quality
- Limited PDF dataset
- No user login system
- Requires internet connection for LLM API