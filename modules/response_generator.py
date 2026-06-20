from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv(
        "GOOGLE_API_KEY"
    )
)


def generate_response(
    persona,
    query,
    retrieved_docs
):

    context=" ".join(
        [
            doc.page_content
            for doc in retrieved_docs
        ]
    )

    prompt=f"""

You are a customer support assistant.

Persona:
{persona}

User Question:
{query}

Context:
{context}

Rules:
- Use ONLY provided context
- Do not invent information
- Adjust response according to persona

"""


    response=client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text