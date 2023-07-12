import requests
from bs4 import BeautifulSoup

OUTPUT_FILE = "output.txt"

def remove_unwanted_tags(soup, unwanted_tags):
    for tag in unwanted_tags:
        for match in soup.findAll(tag):
            match.extract()

def get_raw_content(url, outputFile):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    content_div = soup.find('div', {'class': 'mw-parser-output'})

    unwanted_tags = ['sup', 'span', 'table', 'ul', 'ol']
    remove_unwanted_tags(content_div, unwanted_tags)

    text = content_div.get_text().replace('\n', '')

    with open(outputFile, 'w', encoding='utf-8') as file:
        file.write(text)

    return text

def load_document(pathfile):
  # load the document
  with open(pathfile, encoding='utf-8') as f:
      text = f.read()

  return text


def get_content(url, get_raw=True):
  if get_raw:
    content = get_raw_content(url, OUTPUT_FILE)
  else:
    content = load_document(OUTPUT_FILE)

  return content