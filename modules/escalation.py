def check_escalation(query):

    sensitive_words=[
        "billing",
        "legal",
        "account",
        "refund"
    ]

    query=query.lower()

    if any(
        word in query
        for word in sensitive_words
    ):
        return True

    return False