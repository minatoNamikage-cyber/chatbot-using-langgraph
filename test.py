import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# 1. Load your .env file
load_dotenv()

# 2. Teri list mein 'gemini-2.5-flash' sabse top par hai
# LangChain mein hum 'models/' prefix hata kar likhte hain
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", 
    temperature=0.7
)

try:
    print("Testing with Gemini 2.5 Flash...")
    response = llm.invoke("Sid is back! Sab set hai na?")
    print("-" * 30)
    print("Success! Response:", response.content)
    print("-" * 30)
except Exception as e:
    # Agar 2.5 fail hua (jo ki nahi hona chahiye), toh 2.0 try karega
    print(f"2.5 mein issue hai, 2.0 try kar raha hoon... Error: {e}")
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
    response = llm.invoke("Sid is back!")
    print("Success with 2.0! Response:", response.content)