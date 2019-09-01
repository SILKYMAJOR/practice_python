BANNER = '''
{a} _____{b} _____{c} __   {d} _____{e} __ __   {f} _____{g} _____{h}    __{i} _____{j} _____ 
{a}|   __{b}|     {c}|  |  {d}|  |  {e}|  |  |  {f}|     {g}|  _  {h}|__|  {i}|     {j}| __  |
{a}|__   {b}|-   -{c}|  |__{d}|    -{e}|_   _|  {f}| | | {g}|     {h}|  |  {i}|  |  {j}|    -|
{a}|_____{b}|_____{c}|_____{d}|__|__|{e} |_|    {f}|_|_|_{g}|__|__{h}|_____{i}|_____{j}|__|__|
'''


class Color:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    END = '\033[0m'
    BOLD = '\038[1m'
    UNDERLINE = '\033[4m'
    INVISIBLE = '\033[08m'
    REVERCE = '\033[07m'


def main():
    print(BANNER.format(
        a=Color.RED,
        b=Color.YELLOW,
        c=Color.GREEN,
        d=Color.CYAN,
        e=Color.BLUE,
        f=Color.RED,
        g=Color.YELLOW,
        h=Color.GREEN,
        i=Color.CYAN,
        j=Color.BLUE
    ))


if __name__ == '__main__':
    main()
