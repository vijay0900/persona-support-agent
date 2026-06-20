def detect_persona(query):

    technical_words = [
        "api",
        "logs",
        "configuration",
        "authentication"
    ]

    frustrated_words = [
        "nothing works",
        "tried everything",
        "angry",
        "frustrated"
    ]

    business_words = [
        "impact",
        "revenue",
        "operations",
        "business"
    ]

    query=query.lower()

    if any(word in query for word in technical_words):
        return "Technical Expert"

    elif any(word in query for word in frustrated_words):
        return "Frustrated User"

    elif any(word in query for word in business_words):
        return "Business Executive"

    return "General User"