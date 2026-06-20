from modules.escalation import check_escalation
from modules.handoff import create_handoff


query="I have a billing dispute"

escalate=check_escalation(
    query
)

print(
    "Escalation:",
    escalate
)

if escalate:

    summary=create_handoff(
        "Business Executive",
        query,
        ["billing.txt"]
    )

    print(summary)