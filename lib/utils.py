import tiktoken

def num_tokens_from_string(string: str, encoding_name: str = "cl100k_base") -> int:
  """Returns the number of tokens in a text string."""
  encoding = tiktoken.get_encoding(encoding_name)
  num_tokens = len(encoding.encode(string))
  return num_tokens

def get_pricing_token(tokens: int, price_per_1k_token: float = 0.0001) -> float:
    """Returns the price of a given number of tokens."""
    return tokens * price_per_1k_token / 1000.0

def calculate_insights(title:str, text: str):
  tokens = num_tokens_from_string(text)
  price = get_pricing_token(tokens)

  print(f"-> Insights for {title}")
  print("Amount of tokens: ", tokens)
  print("Price approx: $", price)