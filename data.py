HEADERS = {
    'url': 'https://urban-university.ru/members/login',
    'url_course': 'https://urban-university.ru/members/courses/course999421818026/'
                  'vvodnyj-urok-po-kursu-pythonrazrabotcik-261537127731',
    'host': 'https://urban-university.ru',
    'login': '***@***.ru',
    'password': '********',
    'file_name': 'file_source.html',
    'directory': 'home_works',
    'key_works': ['Самостоятельная работа', 'Домаш', 'Практическое задание',
                  'Практическая работа', 'Дополнительное практическое задание']
}


def save_source(file_name, data_source):
    """
        Сохранение данных в файл
    :param file_name: имя файла
    :param data_source: блок данных
    :return:
    """
    with open(file_name, 'w', encoding='utf8') as file:
        file.write(data_source)


def read_source(file_name):
    """
        Чтение данных
    :param file_name: имя файла
    :return:
    """
    with open('file_source.html', 'r', encoding='utf8') as file:
        data_source = file.read()
    return data_source

