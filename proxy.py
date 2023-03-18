import time

from imports import *


def get_free_proxies():
    print("Get proxies...")
    proxies = free_proxy_list_net()
    proxies += free_proxy_cz()
    proxies += advanced_name()
    print(f'Detected free proxies - {len(set(proxies))}:')
    return list(set(proxies))


def free_proxy_list_net():
    url = "https://free-proxy-list.net/"
    soup = bs4.BeautifulSoup(requests.get(url).content, "html.parser")
    proxies = []
    for row in soup.find("table", attrs={"class": "table table-striped table-bordered"}).find_all("tr")[1:]:
        tds = row.find_all("td")
        try:
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            host = f"{ip}:{port}"
            proxies.append(host)
        except IndexError:
            continue
    return proxies


def advanced_name():
    proxies = []
    for page in range(1, 3):
        url = "https://advanced.name/freeproxy?type=https&page=" + str(page)
        soup = bs4.BeautifulSoup(requests.get(url).content, "html.parser")

        for row in soup.find("table", attrs={"id": "table_proxies"}).find_all("tr")[1:]:
            tds = row.find_all("td")
            try:
                ip = tds[1].text.strip()
                port = tds[2].text.strip()
                host = f"{ip}:{port}"
                proxies.append(host)
            except IndexError:
                continue

        time.sleep(1)
    return proxies


def free_proxy_cz():
    proxies = []
    for page in range(1, 6):
        print(page)
        url = "http://free-proxy.cz/ru/proxylist/country/all/https/ping/all/" + str(page)
        soup = bs4.BeautifulSoup(requests.get(url).content, "html.parser")

        for row in soup.find("table", attrs={"id": "proxy_list"}).find_all("tr")[1:]:
            tds = row.find_all("td")
            try:
                ip = tds[0].text.strip()
                port = tds[1].text.strip()
                host = f"{ip}:{port}"
                proxies.append(host)
            except IndexError:
                continue

        time.sleep(1)
    return proxies


class ProxyParser:
    def __init__(self):
        self.all_available_proxy = []

    def __call__(self, *args, **kwargs):
        self.all_available_proxy = get_free_proxies()
