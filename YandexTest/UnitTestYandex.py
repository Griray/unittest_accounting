import unittest
import requests

oauth_token = input("Введите OAUTH token ")


class Testation(unittest.TestCase):
    def setUp(self):
        print("method SetUp")

    # Тест на создание новой папки
    def test_creates_directory(self):
        header = {"Authorization": oauth_token}
        response = requests.put("https://cloud-api.yandex.net/v1/disk/resources?path=for%20test", headers=header)
        self.assertEqual(response.status_code, 201)

    # Тест на создание папки без названия
    def test_create_directory_with_empty_name(self):
        header = {"Authorization": oauth_token}
        response = requests.put("https://cloud-api.yandex.net/v1/disk/resources?path=%20", headers=header)
        self.assertEqual(response.status_code, 201)

    # Тест на наличие той или иной папки на Я.Диске
    def test_existance_of_folder(self):
        header = {"Authorization": oauth_token}
        response = requests.get("https://cloud-api.yandex.net/v1/disk/resources?path=for%20test", headers=header)
        self.assertEqual(response.status_code, 200)

    # Тест на наличие несуществующей папки на Я.Диске
    def test_not_existance_of_folder(self):
        header = {"Authorization": oauth_token}
        response = requests.get("https://cloud-api.yandex.net/v1/disk/resources?path=empty", headers=header)
        self.assertEqual(response.status_code, 404)

    # Тест на создание существующей папки
    def test_create_existing_folder(self):
        header = {"Authorization": oauth_token}
        response = requests.put("https://cloud-api.yandex.net/v1/disk/resources?path=for%20test", headers=header)
        self.assertEqual(response.status_code, 409)

    # Тест с ожидаемым Fail на создание существующей папки
    @unittest.expectedFailure
    def test_wrong_create_existing_folder(self):
        header = {"Authorization": oauth_token}
        response = requests.put("https://cloud-api.yandex.net/v1/disk/resources?path=for%20test", headers=header)
        self.assertEqual(response.status_code, 201)

    def tearDown(self):
        print("method tearDown")

    def tearDownClass(cls):
        print("method tearDownClass")