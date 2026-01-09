import google.generativeai as genai
from embed_docs import search

genai.configure(api_key="YOUR_GEMINI_API_KEY")
model = genai.GenerativeModel("models/gemini-2.5-flash")

print("Ask questions about your documents (type 'exit' to quit)\n")

while True:
    question = input("You: ")
    if question.lower() == "exit":
        break

    relevant_chunks = search(question)

    context = "\n".join(relevant_chunks)

    prompt = f"""
Answer the question using ONLY the context below.

Context:
{context}

Question:
{question}
"""

    response = model.generate_content(prompt)
    print("Bot:", response.text.strip())
