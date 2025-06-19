from transformers import MarianMTModel, MarianTokenizer
import torch

# Step 1: Load pre-trained English→Chinese model
model_name = 'Helsinki-NLP/opus-mt-en-zh'
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

# Step 2: Prepare your English text (trimmed for demo)
from extract_article_text import fetch_article_text
article_text = fetch_article_text("History")
text_to_translate = article_text[:512]  # MarianMT handles up to ~512 tokens

# Step 3: Tokenize and translate
inputs = tokenizer([text_to_translate], return_tensors="pt", padding=True)
translated = model.generate(**inputs)

# Step 4: Decode output
translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
print("🔁 Translated Text:\n")
print(translated_text)
