from modules.search_engine import search_documents

query="How do I reset my password?"

results=search_documents(query)

for i,result in enumerate(results):

    print("\nResult",i+1)
    print(result.page_content)