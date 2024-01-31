def draw(elem: str) -> None:
    print(9 * '-')
    print(' '.join(list(f'|{elem[0:3]}|')))
    print(' '.join(list(f'|{elem[3:6]}|')))
    print(' '.join(list(f'|{elem[6:9]}|')))
    print(9 * '-')


def analyze(string: str) -> str:
    symbols = ('X', 'O')
    res = ''
    for s in symbols:
        if string[0:3].count(s) == 3:
            res += s
        if string[3:6].count(s) == 3:
            res += s
        if string[6:9].count(s) == 3:
            res += s

        if string[0:9:3].count(s) == 3:
            res += s
        if string[1:9:3].count(s) == 3:
            res += s
        if string[2:9:3].count(s) == 3:
            res += s

        if string[0:9:4].count(s) == 3:
            res += s
        if string[6:1:-2].count(s) == 3:
            res += s

    if len(res) == 1:
        return res
    elif len(res) == 2:
        return ""

    n = string.count('X') - string.count('O')
    if not (n in (0, 1)):
        return ""

    if string.count('_'):
        return '_'

    return 'Draw'


inp = input()
draw(inp)
match analyze(inp):
    case 'X':
        print('X wins')
    case 'O':
        print('O wins')
    case '_':
        print('Game not finished')
    case '':
        print('Impossible')
    case _:
        print('Draw')
