import logging
import concurrent.futures

# logging.basicConfig(
#     level=logging.DEBUG, format='%(threadName)s: %(message)s'
# )

logging.basicConfig(
    level=logging.DEBUG, format='%(processName)s: %(message)s'
)


def worker(x, y):
    logging.debug('start')
    r = x * y
    logging.debug(r)
    logging.debug('end')
    return r


def sample_threading():
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        f1 = executor.submit(worker, 2, 5)
        f2 = executor.submit(worker, 2, 5)
        logging.debug(f1.result())
        logging.debug(f2.result())

        # map sample
        args = [[2, 2], [5, 5]]
        r = executor.map(worker, *args)
        logging.debug(r)
        logging.debug([i for i in r])


def sample_multiprocessing():
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        f1 = executor.submit(worker, 2, 5)
        f2 = executor.submit(worker, 2, 5)
        logging.debug(f1.result())
        logging.debug(f2.result())

        # map sample
        args = [[2, 2], [5, 5]]
        r = executor.map(worker, *args)
        logging.debug(r)
        logging.debug([i for i in r])


def main():
    # sample_threading()
    sample_multiprocessing()


if __name__ == '__main__':
    main()
