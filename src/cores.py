from curses import color_pair


# 'reset': '\x1b[0m'
cores = {
    'black': 1, 'blue': 5, 'cyan': 7, 'green': 3, 'red': 2,
    'white': 0, 'yellow': 4, 'purple': 6, 'gray': 9, 'light_green': 11,
    'light_white': 8,
}


def cor(cor: str):
    return color_pair(cores[cor])
