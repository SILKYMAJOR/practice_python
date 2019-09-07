import logging
import multiprocessing
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(processName)s: %(message)s'
)


def process(i):
    logging.debug('start')
    time.sleep(2)
    logging.debug('end')
    return i


def f():
    with multiprocessing.Pool(5) as p:
        print('Execute Sync Process')
        logging.debug(p.apply(process, (0,)))

        print('Execute Async Process')
        p1 = p.apply_async(process, (1,))
        p2 = p.apply_async(process, (2,))
        p3 = p.apply_async(process, (3,))

        logging.debug(p1.get())
        logging.debug(p2.get())
        logging.debug(p3.get())


def f2():
    print("[*]map")
    with multiprocessing.Pool(5) as p:
        r = p.map(process, [1, 2, 3])
        logging.debug('Executed')
        logging.debug(r)

    print("[*]map_async")
    with multiprocessing.Pool(5) as p:
        r = p.map_async(process, [1, 2, 3])
        logging.debug('Executed')
        logging.debug(r.get())

    print("[*]imap")
    with multiprocessing.Pool(5) as p:
        r = p.imap(process, [1, 2, 3])
        logging.debug([i for i in r])


def main():
    # f()
    f2()


if __name__ == '__main__':
    main()

