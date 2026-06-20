from modules.persona_detector import detect_persona
from modules.search_engine import search_documents
from modules.response_generator import generate_response


query="Can you explain API authentication problem?"

persona=detect_persona(query)

results=search_documents(query)

response=generate_response(
    persona,
    query,
    results
)

print("\nPersona:")
print(persona)

print("\nAI Response:")
print(response)