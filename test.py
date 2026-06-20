from modules.persona_detector import detect_persona

message="Can you explain API authentication issue?"

result=detect_persona(message)

print("Detected Persona:")
print(result)