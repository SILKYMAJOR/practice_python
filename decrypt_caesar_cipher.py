def decrypt(cipher_text, key):
    ret = ""

    for ch in list(cipher_text):
        if 'A' <= ch <= 'Z':
            ret += chr((ord(ch) - ord('A') + key) % 26 + ord('A'))
        elif 'a' <= ch <= 'z':
            ret += chr((ord(ch) - ord('a') + key) % 26 + ord('a'))
        else:
            ret += ch

    return ret


def main():
    cipher_text = input("Enter Caesar cipher : ")

    for i in range(1, 26):
        print('{0:2d}'.format(i) + " : " + decrypt(cipher_text, i))


if __name__ == '__main__':
    main()