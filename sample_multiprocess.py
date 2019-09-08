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


def lock_process(data, lock):
    logging.debug(id(data))
    with lock:
        i = data['x']
        time.sleep(2)
        data['x'] = i + 1
    logging.debug(str(data) + str(id(data)))


def sample_lock():
    data = {'x': 0}
    print('data id :', id(data))
    lock = multiprocessing.Lock()
    # data is not shared , but id is the same.
    t1 = multiprocessing.Process(target=lock_process, args=(data, lock))
    t2 = multiprocessing.Process(target=lock_process, args=(data, lock))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    logging.debug(str(data) + str(id(data)))


def process_pipe(conn):
    conn.send(['message'])
    time.sleep(5)
    conn.close()


def sample_pipe():
    parent_conn, child_conn = multiprocessing.Pipe()
    p = multiprocessing.Process(target=process_pipe, args=(parent_conn, ))
    p.start()
    logging.debug(child_conn.recv())


def process_value_array(num, arr):
    logging.debug(num)
    num.value += 1.0
    logging.debug(arr)
    for i in range(len(arr)):
        arr[i] *= 2


def sample_value_array():
    num = multiprocessing.Value('f', 0.0)
    arr = multiprocessing.Array('i', [1, 2, 3, 4, 5])

    p1 = multiprocessing.Process(target=process_value_array, args=(num, arr))
    p2 = multiprocessing.Process(target=process_value_array, args=(num, arr))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    logging.debug(num.value)
    logging.debug(arr[:])


def process_manager(l, d, n):
    l.reverse()
    d['x'] += 1
    n.y += 1


def sample_manager():
    # Manager is later than Value, Array.
    with multiprocessing.Manager()as manager:
        l = manager.list()
        d = manager.dict()
        n = manager.Namespace()

        l.append(1)
        l.append(2)
        l.append(3)
        d['x'] = 0
        n.y = 0

        p1 = multiprocessing.Process(target=process_manager, args=(l, d, n))
        p2 = multiprocessing.Process(target=process_manager, args=(l, d, n))

        p1.start()
        p2.start()

        p1.join()
        p2.join()

        logging.debug(l)
        logging.debug(d)
        logging.debug(n)


def main():
    # f()
    # f2()
    # sample_lock()
    # sample_pipe()
    # sample_value_array()
    sample_manager()


if __name__ == '__main__':
    main()

