import os
from langchain import PromptTemplate, OpenAI

OPENAI_KEY = os.getenv('OPENAI_API_KEY')

def create_prompt_context(results, question_text):

  # define the prompt template
  template = """
  Eres un chatbot que ama ayudar a las personas. Dado los siguientes fragmentos de contexto,
  responde la pregunta utilizando solamente el contexto proporcionado. La respuesta debe ser una oración.
  Si no estás seguro y la respuesta no está escrita explícitamente en la documentación,
  di "Lo siento, no sé cómo ayudarte con eso"."

  Secciones de contexto:
  {context}

  Pregunta:
  {question}

  Respuesta:
  """

  prompt = PromptTemplate(template=template, input_variables=["context", "question"])

  # fill the prompt template
  return prompt.format(context=results, question=question_text)


def send_prompt(key, results, users_question):

  prompt_text = create_prompt_context(results, users_question)
  llm =  OpenAI(openai_api_key=key, temperature=1)

  return llm(prompt_text)