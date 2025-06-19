import wikipediaapi
from bs4 import BeautifulSoup
import requests

def fetch_article_text(title: str, lang: str = "en") -> str:
    wiki_wiki = wikipediaapi.Wikipedia(language =lang,user_agent="SymmetryTranslatorBot/1.0 (StellaPng; for academic research)")
    page = wiki_wiki.page(title)

    if not page.exists():
        print(f"❌ Page '{title}' does not exist in language '{lang}'.")
        return ""

    return page.text

if __name__ == "__main__":
    article_title = "History"
    article_text = fetch_article_text(article_title)
    print(article_text[:1000])  # Print the first 1000 characters
