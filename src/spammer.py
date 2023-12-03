import multiprocessing as mp
import requests

from src.config import getJSON


class Spammer():
    def __init__(self):
        self.config = getJSON()
        self.url = self.config.get('url')
        self.method = self.config.get('method')
        self.headers = self.config.get('headers')
        self.data = self.config.get('data')
        self.show_response = False

    def function(self, amount: int):
        for _ in range(amount):
            if self.method.upper() == 'GET':
                r = requests.get(self.url, headers=self.headers, data=self.data)
            elif self.method.upper() == 'DELETE':
                r = requests.delete(self.url, headers=self.headers, data=self.data)
            elif self.method.upper() == 'HEAD':
                r = requests.head(self.url, headers=self.headers, data=self.data)
            elif self.method.upper() == 'OPTIONS':
                r = requests.options(self.url, headers=self.headers, data=self.data)
            elif self.method.upper() == 'PATCH':
                r = requests.patch(self.url, headers=self.headers, data=self.data)
            elif self.method.upper() == 'POST':
                r = requests.post(self.url, headers=self.headers, data=self.data)
            elif self.method.upper() == 'PUT':
                r = requests.put(self.url, headers=self.headers, data=self.data)
            else:
                raise ValueError("[ERROR] HTTP request method is invalid")
            print(f"[LOG] {r.status_code}")
            if self.show_response:
                print(f"[LOG] {r.text}")

    def spam(self):
        pool = mp.Pool(mp.cpu_count())
        pool.map(self.function, range(0, 100))

    def send(self):
        self.function(1)
