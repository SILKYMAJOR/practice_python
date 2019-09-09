from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


def main():
    QueueManager.register('get_queue')

    manager = QueueManager(
        address=('127.0.0.1', 50000),
        authkey=b'basemanager'
    )
    manager.connect()
    queue = manager.get_queue()
    queue.put('hello')


if __name__ == '__main__':
    main()
