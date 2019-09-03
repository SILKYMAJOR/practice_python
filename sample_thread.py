import time
import threading


def thread(num):
    print("Thread Start {}".format(num))
    time.sleep(2)
    print("Thread End {}".format(num))


def sample():
    for i in range(1, 4):
        threading.Thread(target=thread, name="th", args=(i,)).start()


def main():
    sample()


if __name__ == '__main__':
    main()
