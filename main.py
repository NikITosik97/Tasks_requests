import requests
import os


def search_superhero():
    url = 'https://akabab.github.io/superhero-api/api//all.json'

    response = requests.get(url)

    all_heroes = response.json()

    heroes = []

    for hero in all_heroes:
        if 'Hulk' in hero['name']:
            heroes.append([hero['powerstats']['intelligence'], hero['name']])
        if 'Captain America' in hero['name']:
            heroes.append([hero['powerstats']['intelligence'], hero['name']])
        if 'Thanos' in hero['name']:
            heroes.append([hero['powerstats']['intelligence'], hero['name']])

    heroes.sort(reverse=True)

    return print(f'Самый высокий интеллект у героя - {heroes[0][1]}\n'
                 f'Интеллект - {heroes[0][0]}')


search_superhero()


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

        params = {'path': file_path}

        headers = {'Authorization': 'OAuth ' + self.token}

        response = requests.get(url, headers=headers, params=params)

        data = response.json()

        url_upload = data['href']

        with open(file_path, 'rb') as f:
            response = requests.post(url_upload, files={'file': f})


if __name__ == '__main__':
    path_to_file = os.getcwd()
    token = open('token.txt').readline().strip()
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)