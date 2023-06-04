import saving_utils
from article_parser import get_article_content
from main_page_parser import parse_main_page


def main():
    links = parse_main_page()
    results = [{l: get_article_content(l)} for l in links]
    saving_utils.save_to_json(results, 'vc_articles')
    saving_utils.save_to_csv(results, 'vc_articles')


if __name__ == '__main__':
    main()
