import logging
import multiprocessing
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(processName)s: %(message)s'
)


def process1(i):
    logging.debug('start')
    logging.debug(i)
    time.sleep(2)
    logging.debug('end')


def process2(i):
    logging.debug('start')
    logging.debug(i)
    logging.debug('end')


def main():
    i = 10
    m1 = multiprocessing.Process(target=process1, args=(i, ))
    m1.daemon = True
    m2 = multiprocessing.Process(target=process2, name='p2', args=(i, ))

    m1.start()
    m2.start()

    m1.join()
    m1.join()


if __name__ == '__main__':
    main()

