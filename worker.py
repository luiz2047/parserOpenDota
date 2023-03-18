from imports import *


class Worker(multiprocessing.Process):

    def __init__(self,
                 job_queue,
                 free_proxies):
        super().__init__()
        self._job_queue = job_queue
        self._free_proxies = free_proxies
        self._proxy = {
            "https": random.choice(free_proxies)
        }
        self._url = "https://api.opendota.com/api/matches/"

    def change_proxy(self):
        self._proxy = {
            "https": random.choice(self._free_proxies)
        }

    def run(self):
        while True:
            match_id = self._job_queue.get()
            if match_id is None:
                break
            while True:
                try:
                    req = self._url + match_id
                    page = requests.get(req, proxies=self._proxy, verify=False,
                                        timeout=3)
                    if "The page you requested has been blocked by a firewall policy restriction" in str(page.content):
                        raise Exception("Firewall, trying to change proxy...")
                    data_json = json.loads(page.content)
                    with open("full_matches.json", "a+", encoding='utf-8') as f:
                        json.dump(data_json, f)
                        f.write("\n")
                    logging.info(req + ' - Match_id: ' + str(data_json["match_id"]))

                    break
                except requests.exceptions.ReadTimeout as e:
                    logging.debug('TimeOut!')
                    self.change_proxy()
                except requests.exceptions.HTTPError as e:
                    logging.debug('HTTPError')
                    self.change_proxy()
                except requests.exceptions.ProxyError as e:
                    logging.debug('ProxyError')
                    self.change_proxy()
                except requests.exceptions.ConnectionError as e:
                    logging.debug('ConnectTimeoutError')
                    self.change_proxy()
                except Exception as ex:
                    logging.debug(ex)
                    self.change_proxy()
