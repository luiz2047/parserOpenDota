from proxy import *
import worker
import argparse

logging.basicConfig(filename='logs.log', encoding='utf-8', level=logging.DEBUG,
                    format='%(asctime)s %(name)-8s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

urllib3.disable_warnings()


def main(num_workers):
    free_proxies = get_free_proxies()
    jobs = []
    job_queue = multiprocessing.Queue()
    with multiprocessing.Manager() as manager:
        shared_free_proxies = manager.list(free_proxies)
        for i in range(num_workers):
            p = worker.Worker(job_queue, shared_free_proxies)
            jobs.append(p)
            p.start()

        with open('matches_ids.txt', 'r') as urls:
            for url in urls.readlines():
                job_queue.put(url)

        for j in jobs:
            job_queue.put(None)

        for j in jobs:
            j.join()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='parserOpenDota',
        description="""Parsing full matches data using external proxy from OpenDotaAPI 
        using matches_ids.txt file and save it in full_matches.json file"""
    )
    parser.add_argument('-n', '--num_workers', type=int, default=128,
                        help="Num workers for parsing")
    args = parser.parse_args()
    main(args.num_workers)
