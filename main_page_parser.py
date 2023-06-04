import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from div_classes import POST_CLASS, ARTICLE_LINK_CLASS

driver = webdriver.Chrome()


def parse_main_page(scrolls: int = 0):
    """

    :param scrolls:
        Сколько раз нужно пролистать главную страницу вниз
    :return:
        Список ссылок на статьи
    """
    driver.get("https://vc.ru")
    time.sleep(2)

    for i in range(scrolls):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

    post_elems = driver.find_elements(By.CLASS_NAME, POST_CLASS)
    return [post.find_element(By.CLASS_NAME, ARTICLE_LINK_CLASS).get_attribute('href') for post in post_elems]
