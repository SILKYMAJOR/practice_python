import time
import threading


def thread(num):
    print("Thread Start {}".format(num))
    time.sleep(2)
    print("Thread End {}".format(num))


def bad_sample():
    for i in range(300):
        threading.Thread(target=thread(i)).start()


def main():
    pass


if __name__ == '__main__':
    main()