import queue
from multiprocessing.managers import BaseManager

queue = queue.Queue()


class QueueManager(BaseManager):
    pass


def main():

    QueueManager.register(
        'get_queue', callable=lambda: queue
    )

    manager = QueueManager(
        address=('127.0.0.1', 50000),
        authkey=b'basemanager'
    )
    server = manager.get_server()
    server.serve_forever()


if __name__ == '__main__':
    main()
