from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_text_for_document(text):

  text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap  = 20,
    length_function=len)
  return text_splitter.create_documents([text])