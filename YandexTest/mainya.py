import requests

oauth_token = input("Введите OAUTH token ")

def make_new_folder_yandexdisk():
    header = {"Authorization": oauth_token}
    new_folder = requests.put("https://cloud-api.yandex.net/v1/disk/resources?path=for%20test", headers=header)
    print(str(new_folder))
    return str(new_folder)

def check_exist_of_this_folder():
    header = {"Authorization": oauth_token}
    new_folder = requests.get("https://cloud-api.yandex.net/v1/disk/resources?path=for%20test", headers=header)
    print(str(new_folder))
    return str(new_folder)

