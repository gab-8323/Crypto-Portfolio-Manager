import requests
import xml.etree.ElementTree as ET
import html

def get_crypto_news():
    url = "https://cointelegraph.com/rss"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            root = ET.fromstring(response.content)
            news_items = []
            for item in root.findall('.//item')[:5]:
                title = item.find('title').text
                link = item.find('link').text
                # Clean up title and link
                news_items.append({
                    'title': html.unescape(title),
                    'link': link
                })
            return news_items
    except Exception as e:
        print(f"Error fetching news: {e}")
    return []

if __name__ == "__main__":
    news = get_crypto_news()
    for n in news:
        print(f"- {n['title']}\n  {n['link']}\n")
