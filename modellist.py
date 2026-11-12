<<<<<<< HEAD
import os
from dotenv import load_dotenv
from google import genai
load_dotenv()
client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
for model in client.models.list():
    print(model.name)


=======
import os
from dotenv import load_dotenv
from google import genai
load_dotenv()
client=genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
for model in client.models.list():
    print(model.name)


>>>>>>> 01db78518a6ac0279342c326f00d943b80072dac
#use google ai studio for api key for model 