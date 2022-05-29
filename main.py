import requests
import os
import pathlib
from pathlib import Path

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        try:
            open(file_path, 'rb')
        except FileNotFoundError:
            print('Такого пути нет')
            return

        file = pathlib.Path(file_path)

        url = 'https://cloud-api.yandex.net/'
        head = {
            'Authorization': f'OAuth {self.token}'
        }
        method = 'v1/disk/resources/upload'
        param = {
            'path':file.name,
            'overwrite':'true'
        }
        response = requests.get(url+method, headers=head, params=param).json()
        with open(file_path, 'rb') as f:
            try:
                res = requests.put(response['href'], files={'file':f})
                print('Файл закачан')
            except KeyError:
                print('Ошибка закачки')

if __name__ == '__main__':
    print('Введите путь до файла для загрузки \n')
    path_to_file = str(input())
    token = 'AQAAAAAXyByvAAfw_FB933pKPkKMp8vT4zclRCE'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)