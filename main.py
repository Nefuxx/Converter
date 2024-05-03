from bs4 import BeautifulSoup as bs
import requests
from enum import Enum


class Currency(Enum):
    RUB = 1,
    DLL = 2,
    EVR = 3,
    YUAN = 4



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 YaBrowser/24.1.0.0 Safari/537.36'}


class Converter:
    urls = {Currency.DLL: "https://www.google.ru/search?q=rubl+to+dollar&newwindow=1&sca_esv=3e5ddf52b76d97c4&sca_upv=1&ei=P-MoZtKUNJvZwPAPuMmM0Ak&ved=0ahUKEwiSsLSs1tqFAxWbLBAIHbgkA5oQ4dUDCBA&oq=rubl+to+dollar&gs_lp=Egxnd3Mtd2l6LXNlcnAiDnJ1YmwgdG8gZG9sbGFySABQAFgAcAB4AZABAJgBAKABAKoBALgBDMgBAJgCAKACAJgDAOIDBRIBMSBAkgcAoAcA&sclient=gws-wiz-serp",
            Currency.EVR: "https://www.google.ru/search?q=ruble+to+euro&newwindow=1&sca_esv=3e5ddf52b76d97c4&sca_upv=1&ei=GeYoZoWFNfvOwPAPstuZ-AU&oq=rubl+to+eu&gs_lp=Egxnd3Mtd2l6LXNlcnAiCnJ1YmwgdG8gZXUqAggAMgsQABiABBiRAhiKBTILEAAYgAQYkQIYigUyCxAAGIAEGJECGIoFMgcQABiABBgKMgcQABiABBgKMgcQABiABBgKMgcQABiABBgKMgcQABiABBgKMgcQABiABBgKMgcQABiABBgKSK0UUNEIWKsJcAF4AZABAJgBeaAB4AGqAQMwLjK4AQPIAQD4AQGYAgOgAu0BwgIKEAAYsAMY1gQYR8ICDRAAGIAEGLADGEMYigWYAwDiAwUSATEgQIgGAZAGCpIHAzEuMqAHvg8&sclient=gws-wiz-serp",
            Currency.YUAN: "https://www.google.ru/search?q=ruble+to+yuan&newwindow=1&sca_esv=3e5ddf52b76d97c4&sca_upv=1&ei=PuYoZsrdJYb7wPAPt42ZgAY&ved=0ahUKEwjK9IOa2dqFAxWGPRAIHbdGBmAQ4dUDCBA&uact=5&oq=ruble+to+yuan&gs_lp=Egxnd3Mtd2l6LXNlcnAiDXJ1YmxlIHRvIHl1YW4yEBAAGIAEGJECGIoFGEYYggIyBRAAGIAEMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeMggQABgWGB4YDzIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjILEAAYgAQYhgMYigUyHBAAGIAEGJECGIoFGEYYggIYlwUYjAUY3QTYAQFI2zNQ3ARYpDFwAngBkAEAmAF4oAHiBqoBAzEuN7gBA8gBAPgBAZgCCqACigfCAgoQABiwAxjWBBhHwgINEAAYgAQYsAMYQxiKBcICChAAGIAEGEMYigXCAg8QABiABBhDGIoFGEYYggLCAhsQABiABBhDGIoFGEYYggIYlwUYjAUY3QTYAQHCAgsQABiABBiRAhiKBcICBxAAGIAEGAqYAwCIBgGQBgq6BgYIARABGBOSBwMzLjegB-Ez&sclient=gws-wiz-serp"}

    def __init__(self, str):
        self.headers = {'User-Agent': str}

    def parce(self, cur):
        full_page = requests.get(Converter.urls[cur], headers=self.headers)
        soup = bs(full_page.content, 'html.parser')
        convert = soup.find('input', {'class': 'lWzCpb a61j6'})
        return float(convert.attrs['value'])

    def convert(self, first, second, amount):
        if first == Currency.RUB and second == Currency.RUB:
            return amount
        elif first == Currency.RUB:
            return amount * self.parce(second)
        elif second == Currency.RUB:
            return amount / self.parce(second)
        else:
            return  self.parce(second) / self.parce(first) * amount

c = Converter('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 YaBrowser/24.1.0.0 Safari/537.36')

print(c.convert(Currency.RUB, Currency.DLL, 50))

