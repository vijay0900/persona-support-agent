import streamlit as st

from modules.persona_detector import detect_persona
from modules.search_engine import search_documents
from modules.response_generator import generate_response
from modules.escalation import check_escalation
from modules.handoff import create_handoff


st.title("Persona Adaptive Support Agent")

query=st.text_input(
    "Ask your question"
)

if query:

    persona=detect_persona(
        query
    )

    st.write(
        "Detected Persona:",
        persona
    )

    results=search_documents(
        query
    )

    response=generate_response(
        persona,
        query,
        results
    )

    st.subheader(
        "AI Response"
    )

    st.write(
        response
    )

    escalate=check_escalation(
        query
    )

    st.subheader(
        "Escalation Status"
    )

    st.write(
        escalate
    )

    if escalate:

        summary=create_handoff(
            persona,
            query,
            [
                "documents used"
            ]
        )

        st.subheader(
            "Human Handoff"
        )

        st.write(
            summary
        )