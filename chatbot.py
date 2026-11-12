from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    google_api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.5,#when temperature increases the intelligence of model also increases
)

print("Gemini Chatbot")
print("Type 'exit' to quit.\n")

while True:
    question = input("You: ")

    if question.lower() == "exit":
        break

    response = llm.invoke([HumanMessage(content=question)])

    #print("Gemini:", response.content)
    answer=response.content
    print(answer[0]["text"])