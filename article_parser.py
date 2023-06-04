import requests
from bs4 import BeautifulSoup

from div_classes import ARTICLE_TAGS


def get_article_content(url):
    response = requests.get(url)
    response.raise_for_status()  # Проверяем наличие ошибок при запросе
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    article_content = []
    for block in soup.find_all(ARTICLE_TAGS):
        block_type = block.name
        # Если блок является списком, извлекаем каждый элемент списка (тег <li>)
        if block_type in ['ul', 'ol']:
            list_items = block.find_all('li')
            for item in list_items:
                item_text = item.get_text(strip=False)
                article_content.append(('li', item_text))
        else:
            block_text = block.get_text(strip=False)
            article_content.append((block_type, block_text))

    return article_content


if __name__ == '__main__':
    url = 'https://vc.ru/marketing/709910-hochu-zapustit-reklamu-no-moy-sayt-ustarel-na-10-let-chto-mne-delat'
    article_content = get_article_content(url)
    for a in article_content:
        print(a)
