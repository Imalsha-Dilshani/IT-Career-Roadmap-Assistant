import streamlit as st
from typing import List
from agents.orchestrator import run_orchestration
from agents.model_selection import select_model
from agents.clients import call_model

st.set_page_config(page_title="IT Career Roadmap Assistant")
st.title("IT Career Roadmap Assistant")

career = st.selectbox(
    "Target Career",
    ["AI Engineer", "Backend Developer", "DevOps Engineer"]
)

skills = st.text_area("Current Skills (comma-separated)")

use_llm = st.checkbox("Use LLM (Groq / OpenRouter) if configured", value=False)
use_rag = st.checkbox("Enable RAG (ChromaDB) when knowledge base available", value=False)


def heuristic_roadmap(target: str, current_skills: List[str]) -> str:
    current = {s.strip().lower() for s in current_skills}
    sections = []

    if target == "AI Engineer":
        short = [s for s in ["python", "numpy", "pandas"] if s not in current]
        ml = [s for s in ["ml fundamentals", "deep learning", "transformers"] if s not in current]
        infra = [s for s in ["docker", "mlops", "model serving"] if s not in current]
        sections.append(("Immediate skills (1-3 months)", short))
        sections.append(("Core AI skills (3-9 months)", ml))
        sections.append(("Production readiness (6-12 months)", infra))

    if target == "Backend Developer":
        short = [s for s in ["python", "api design", "sql"] if s not in current]
        backend = [s for s in ["web frameworks", "databases", "testing"] if s not in current]
        infra = [s for s in ["docker", "ci/cd", "observability"] if s not in current]
        sections.append(("Immediate skills (1-3 months)", short))
        sections.append(("Core backend skills (3-9 months)", backend))
        sections.append(("Deployment & reliability (6-12 months)", infra))

    if target == "DevOps Engineer":
        short = [s for s in ["linux", "scripting", "git"] if s not in current]
        infra = [s for s in ["kubernetes", "terraform", "ci/cd"] if s not in current]
        monitoring = [s for s in ["prometheus", "logging", "alerts"] if s not in current]
        sections.append(("Immediate skills (1-3 months)", short))
        sections.append(("Infrastructure skills (3-9 months)", infra))
        sections.append(("Monitoring & SRE (6-12 months)", monitoring))

    # Render text
    out_lines = []
    for title, items in sections:
        out_lines.append(f"## {title}")
        if items:
            for it in items:
                out_lines.append(f"- {it}")
        else:
            out_lines.append("- Already covered or no gaps detected")

    out_lines.append("\nResources:")
    out_lines.append("- Official docs, free online courses, hands-on projects")
    out_lines.append("- Build 2-3 portfolio projects and publish on Github")
    return "\n".join(out_lines)


def generate_roadmap(target: str, skills_text: str, use_llm_flag: bool, use_rag_flag: bool) -> str:
    skills = [s.strip() for s in skills_text.split(",")] if skills_text.strip() else []

    if use_llm_flag:
        # Placeholder for LLM integration with Groq / OpenRouter.
        # Use Streamlit secrets only (no environment-variable fallback).
        groq_key = st.secrets.get("GROQ_API_KEY")
        openrouter_key = st.secrets.get("OPENROUTER_API_KEY")
        if not (groq_key or openrouter_key):
            return "LLM integration requested, but no GROQ_API_KEY or OPENROUTER_API_KEY found in Streamlit secrets.\n\n" + heuristic_roadmap(target, skills)
        else:
            # Minimal fallback: still return heuristic roadmap and note keys detected.
            provider = "GROQ" if groq_key else "OpenRouter"
            return f"LLM provider configured: {provider}. (LLM call not implemented in this prototype.)\n\n" + heuristic_roadmap(target, skills)

    if use_rag_flag:
        # Placeholder: a real RAG flow would query ChromaDB for domain docs then
        # pass them to the LLM for grounded answers. Use Streamlit secrets only.
        chroma_cfg = st.secrets.get("CHROMA_URL") or st.secrets.get("CHROMA_API_KEY")
        if not chroma_cfg:
            return "RAG requested, but no Chroma configuration found in Streamlit secrets.\n\n" + heuristic_roadmap(target, skills)
        else:
            return "Chroma configured but RAG not implemented in this prototype.\n\n" + heuristic_roadmap(target, skills)

    # Default heuristic roadmap
    return heuristic_roadmap(target, skills)


if st.button("Generate Roadmap"):
    with st.spinner("Generating roadmap..."):
        result = generate_roadmap(career, skills, use_llm, use_rag)
    st.markdown(result)

    st.divider()
    st.markdown("**Agent demo**")
    st.markdown("Run a small orchestrator -> worker demo that shows structured messages and tool-use.")
    if st.button("Run Agent Demo"):
        with st.spinner("Running agents..."):
            demo = run_orchestration(f"Create career roadmap for {career}")
        st.code(demo)

    st.divider()
    st.markdown("**Model selection demo**")
    st.markdown("Shows which model is chosen per sub-task and runs a simulated call using Streamlit secrets.")
    if st.button("Run Model Selection Demo"):
        with st.spinner("Selecting models and calling clients..."):
            subtasks = ["intent_routing", "retrieval_rerank", "final_synthesis"]
            results = {}
            for stask in subtasks:
                entry = select_model(stask)
                provider = entry.get("provider")
                model = entry.get("model")
                prompt = f"Demo prompt for {stask}: give short output."
                call_result = call_model(provider, model, prompt)
                results[stask] = {"selection": entry, "call_result": call_result}
        st.json(results)

    st.divider()
    st.markdown("**Next steps (suggested):**")
    st.markdown("- Configure GROQ_API_KEY / OPENROUTER_API_KEY to enable LLMs")
    st.markdown("- Ingest domain docs into ChromaDB and enable RAG for grounded answers")
