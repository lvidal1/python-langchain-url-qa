
import os
from dotenv import load_dotenv

from lib.database import get_vector_db, search
from lib.prompt import send_prompt

from lib.document import split_text_for_document
from lib.source import get_content
from lib.utils import calculate_insights

OUTPUT_FILE = "output.txt"

PERSIST = False
GET_RAW = False

load_dotenv()

OPENAI_KEY = os.getenv('OPENAI_API_KEY')

print("Fuente:")
url = input()

print("Pregunta:")
users_question = input()

content = get_content(url,GET_RAW)

calculate_insights("Embeddings", content)

documents = split_text_for_document(content)

db = get_vector_db(OPENAI_KEY, documents, PERSIST)

results = search(db, query=users_question,results=5)

response = send_prompt(OPENAI_KEY,results,users_question)

calculate_insights("Response", response)

print(response)