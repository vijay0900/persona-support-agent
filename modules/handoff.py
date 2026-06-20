def create_handoff(
    persona,
    query,
    documents
):

    summary={

        "persona":persona,

        "issue":query,

        "documents_used":documents,

        "recommendation":
        "Human review required"

    }

    return summary