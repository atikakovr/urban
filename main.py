"""
    Задача(решение в функциональном стиле):
    (Использован пакет selenium - в основном используемый для тестирования, но в данной задаче - упростил решение...)
    - открыть сайт урбан...;
    - пройти регистрацию;
    - выйти на урок и получить список заданий из бокового меню: создав словарь;
    - в цикле (анализ словаря) получить ссылки на ДЗ;
    - получив html разметку ДЗ:
        - получить статус задания:
            - если нет его: получить текст задания;
            - иначе: получить решение.
        - по результату создать файл .py в формате:
            - в комментарии:
                - заголовок ДЗ;
                - если есть: описание задания;
            - в теле:
                - если есть: решение.(не отслеживалось, если решение в виде ссылки на git или на архив)
    в data.py:
        Определены:
            - константа(в виде списка)
            - две функции работы с файлами.

    Как доп. задание(не решалась в данном проекте):
        - заливка готовых - решенных задач, на сайт.
"""
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from data import *
import re


def get_content(html):
    """
        Анализ страницы на домашние задания
    :param html: анализируемая html страничка
    :return: список словарей модулей
    """
    soup = BeautifulSoup(html, 'html.parser')
    content_items = []
    for item in soup.find_all('div', class_='tlk-menu__list-item'):
        title_module = item.find('div', class_='tlk-menu__title').get_text(strip=True)
        submenu = []
        item_submenu = item.find_all('div', class_='tlk-menu__submenu-item')

        for i in item_submenu:
            title = i.find('a', class_='tlk-menu__link').get_text(strip=True)
            title = re.sub(' +', ' ', title[title.rfind('|') + 1:].replace('\n', ' '))
            if any(item in title for item in HEADERS['key_works']):
                submenu.append(
                    {
                        'title': title,
                        'href': HEADERS['host'] + i.find('a', class_='tlk-menu__link').get('href'),
                    }
                )
        content_items.append(
            {
                'title': title_module,
                'sub_menu': submenu
            }
        )
    return content_items


def get_content_hw(directory, html, count_content, count_sub):
    """
        Анализ страниц домашних заданий
    :param directory: директория выходных файлов
    :param html: анализируемая html страничка
    :param count_content: относительный номер модуля
    :param count_sub: номер задания
    :return:
    """
    try:
        soup = BeautifulSoup(html, 'html.parser')
        title_work = soup.find('div', class_='tlk-lecture__homework-lecture-title').get_text(strip=True)
        title_status = soup.find('div', class_='tlk-lecture__status').get_text(strip=True)
        solving_problem = ''

        if title_status:
            solving_problem = soup.find('div', class_='tlk-lecture__homework-result-text').get_text('\n')
        else:
            title_status = soup.find('div', class_='tlk-lecture__homework-text').get_text('\n')
            regex = re.compile('((?!\n)\s+)')

            title_status = regex.sub(' ', title_status)

        heading_py = f'"""\n{title_work}\n{title_status}\n"""\n{solving_problem}'
        save_source(f'{directory}hw_{count_content, count_sub}.py', heading_py)
    except Exception as ex:
        print('Какая то ошибка: ', ex)


def run_parser():
    useragent = UserAgent()
    options = webdriver.ChromeOptions()
    options.add_argument(f'user-agent={useragent.edge}')
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url=HEADERS.get('url'))
        time.sleep(5)

        login_input = driver.find_element(By.NAME, 'login')
        login_input.clear()
        login_input.send_keys(HEADERS.get('login'))
        pass_input = driver.find_element(By.NAME, 'password')
        pass_input.clear()
        pass_input.send_keys(HEADERS.get('password'))
        time.sleep(5)
        driver.find_element(By.CLASS_NAME, 'tlk-btn').click()
        time.sleep(5)

        driver.get(url=HEADERS.get('url_course'))
        time.sleep(5)

        contents = get_content(driver.page_source)
        directory = os.path.dirname(__file__) + '\\' + HEADERS['directory'] + '\\'

        if contents:
            if not os.path.exists(directory):
                os.makedirs(directory)

            for count_content, content_modul in enumerate(contents, start=1):
                print(content_modul['title'])

                for count_sub, sub_content in enumerate(content_modul['sub_menu'], start=1):
                    print(' '*4, sub_content['title'])

                    if sub_content['href']:
                        driver.get(url=sub_content['href'])
                        time.sleep(5)
                        get_content_hw(directory, driver.page_source, count_content, count_sub)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
        print('\nЗавершено')


if __name__ == '__main__':
    run_parser()
