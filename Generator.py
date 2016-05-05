#coding: utf8
# quu..__
#  $$$b  `---.__
#   "$$b        `--.                          ___.---uuudP
#    `$$b           `.__.------.__     __.---'      $$$$"              .
#      "$b          -'            `-.-'            $$$"              .'|
#        ".                                       d$"             _.'  |
#          `.   /                              ..."             .'     |
#            `./                           ..::-'            _.'       |
#             /                         .:::-'            .-'         .'
#            :                          ::''\          _.'            |
#           .' .-.             .-.           `.      .'               |
#           : /'$$|           .@"$\           `.   .'              _.-'
#          .'|$u$$|          |$$,$$|           |  <            _.-'
#          | `:$$:'          :$$$$$:           `.  `.       .-'
#          :                  `"--'             |    `-.     \
#         :##.       ==             .###.       `.      `.    `\
#         |##:                      :###:        |        >     >
#         |#'     `..'`..'          `###'        x:      /     /
#          \                                   xXX|     /    ./
#           \                                xXXX'|    /   ./
#           /`-.                                  `.  /   /
#          :    `-  ...........,                   | /  .'
#          |         ``:::::::'       .            |<    `.
#          |             ```          |           x| \ `.:``.
#          |                         .'    /'   xXX|  `:`M`M':.
#          |    |                    ;    /:' xXXX'|  -'MMMMM:'
#          `.  .'                   :    /:'       |-'MMMM.-'
#           |  |                   .'   /'        .'MMM.-'
#           `'`'                   :  ,'          |MMM<
#             |                     `'            |tbap\
#              \                                  :MM.-'
#               \                 |              .''
#                \.               `.            /
#                 /     .:::::::.. :           /
#                |     .:::::::::::`.         /
#                |   .:::------------\       /
#               /   .''               >::'  /
#               `',:                 :    .'

import sys

bridges = ['o-o-o', "|\| |", "o-o o"]  # хранит мосты
leftEdge = '|  '            # всякие паттерны тут
leftEdgeAlt = '| |'
leftIslands = "o-o-o"


def m_five(n):
    if n == 4:
        for i in range(3, 7):
            bridges.append('')
        bridges[0] = 'o-o-o-o-o'
        bridges[1] = '|\ \|/ /|'
        bridges[2] = 'o-o o o-o'
        bridges[3] = '| |   | |'
        bridges[4] = 'o-o o o-o'
        bridges[5] = '|/ /|\ \|'
        bridges[6] = 'o-o-o-o-o'
    else:
        for i in range(3, n * 2 - 1):
            bridges.append('')
        bridges[0] += '-o-o'
        bridges[1] += ' |\|'
        bridges[2] += ' o-o'
        bridges[3] = '|  / \  |'
        bridges[4] = bridges[0]
        for i in range(5, n * 2 - 6):
            if i % 4 == 1:
                bridges[i] = '|   |   |'
            elif i % 2 == 0:
                bridges[i] = bridges[0]
            else:
                bridges[i] = '| |   | |'
        bridges[2 * n - 6] = bridges[0]
        bridges[2 * n - 5] = '|  \ /  |'
        bridges[2 * n - 4] = bridges[2]
        bridges[2 * n - 3] = '|\| | |/|'
        bridges[2 * n - 2] = bridges[0]


def m_uneven(m, n):
    while bridges[0].__len__() != m * 2 - 1:
        bridges[0] += '-o'
    while bridges[1].__len__() != m * 2 - 3:
        bridges[1] += ' |'
    bridges[1] += '/|'
    while bridges[2].__len__() != m * 2 - 5:
        bridges[2] += '-o'
    bridges[2] += ' o-o'
    for i in range(3, n * 2 - 1):
        bridges.append('')
    for i in range(3, n * 2 - 4):
        if i % 2 == 0:
            bridges[i] = leftIslands
            while bridges[i].__len__() != m * 2 - 1:
                bridges[i] += '-o'
        else:
            if i % 4 == 1:
                bridges[i] = leftEdgeAlt
                while bridges[i].__len__() != m * 2 - 4:
                    bridges[i] += ' '
                bridges[i] += '| |'
            else:
                bridges[i] = leftEdge
                while bridges[i].__len__() != m * 2 - 5:
                    bridges[i] += ' |'
                bridges[i] += '   |'
    bridges[n * 2 - 4] = bridges[2]
    bridges[n * 2 - 3] = '|/| |'
    while bridges[n * 2 - 3].__len__() != m * 2 - 3:
        bridges[n * 2 - 3] += ' |'
    bridges[n * 2 - 3] += '\|'
    bridges[n * 2 - 2] = bridges[0]


def n_five(m):
    for i in range(3, 9):
        bridges.append('')
    if m == 4:
        bridges[0] = 'o-o-o-o'
        bridges[1] = '|\| |/|'
        bridges[2] = 'o o-o o'
        bridges[3] = '|\   /|'
        bridges[4] = 'o-o o-o'
        bridges[5] = '|/   \|'
        bridges[6] = 'o o-o o'
        bridges[7] = '|/| |\|'
        bridges[8] = 'o-o-o-o'
    else:
        while bridges[0].__len__() != m * 2 - 1:
            bridges[0] += '-o'
        while bridges[1].__len__() != m * 2 - 3:
            bridges[1] += ' |'
        bridges[1] += '/|'
        while bridges[2].__len__() != m * 2 - 5:
            if bridges[2].__len__() % 4 == 3:
                bridges[2] += '-o'
            else:
                bridges[2] += ' o'
        bridges[2] += ' o-o'
        bridges[3] = '|  /|'
        while bridges[3].__len__() != m * 2 - 5:
            bridges[3] += ' |'
        bridges[3] += '\  |'
        bridges[4] = 'o-o'
        while bridges[4].__len__() != m * 2 - 1:
            if bridges[4].__len__() % 4 == 3:
                bridges[4] += ' o'
            else:
                bridges[4] += '-o'
        bridges[5] = '|  \|'
        while bridges[5].__len__() != m * 2 - 5:
            bridges[5] += ' |'
        bridges[5] += '/  |'
        bridges[6] = bridges[2]
        bridges[7] = '|/|'
        while bridges[7].__len__() != m * 2 - 3:
            bridges[7] += ' |'
        bridges[7] += '\|'
        bridges[8] = bridges[0]


def n_uneven(m, n):
    while bridges[0].__len__() != m * 2 - 1:
        bridges[0] += '-o'
    while bridges[1].__len__() != m * 2 - 3:
        bridges[1] += ' |'
    bridges[1] += '/|'
    while bridges[2].__len__() != m * 2 - 1:
        if bridges[2].__len__() % 4 == 3:
            bridges[2] += ' o'
        else:
            bridges[2] += '-o'
    for i in range(3, n * 2 - 1):
        bridges.append('')
    for i in range(3, n):
        if i % 2 == 0:
            bridges[i] = leftIslands
            while bridges[i].__len__() != m * 2 - 3:
                if bridges[i].__len__() % 4 == 3:
                    bridges[i] += '-o'
                else:
                    bridges[i] += ' o'
            bridges[i] += '-o'
        else:
            if i % 4 == 1:
                bridges[i] = leftEdgeAlt
                while bridges[i].__len__() != m * 2 - 1:
                    bridges[i] += ' |'
            else:
                bridges[i] = leftEdge
                while bridges[i].__len__() != m * 2 - 5:
                    bridges[i] += ' |'
                bridges[i] += '   |'
    for i in range(n, 2 * n - 3):
        bridges[i] = bridges[2 * n - i - 2]
    bridges[n * 2 - 3] = '|/| |'
    while bridges[n * 2 - 3].__len__() != m * 2 - 3:
        bridges[n * 2 - 3] += ' |'
    bridges[n * 2 - 3] += '\|'
    bridges[n * 2 - 2] = bridges[0]


def all_even(m, n):
    while bridges[0].__len__() != m * 2 - 1:
        bridges[0] += '-o'
    while bridges[1].__len__() != m * 2 - 3:
        bridges[1] += ' |'
    bridges[1] += '/|'
    while bridges[2].__len__() != m * 2 - 1:
        if bridges[2].__len__() % 4 == 3:
            bridges[2] += ' o'
        else:
            bridges[2] += '-o'
    for i in range(3, n * 2 - 1):
        bridges.append('')
    for i in range(3, n * 2 - 4):
        if i % 2 == 0:
            bridges[i] = leftIslands
            while bridges[i].__len__() != m * 2 - 3:
                if bridges[i].__len__() % 4 == 3:
                    bridges[i] += '-o'
                else:
                    bridges[i] += ' o'
            bridges[i] += '-o'
        else:
            if i % 4 == 1:
                bridges[i] = leftEdgeAlt
                while bridges[i].__len__() != m * 2 - 1:
                    bridges[i] += ' |'
            else:
                bridges[i] = leftEdge
                while bridges[i].__len__() != m * 2 - 5:
                    bridges[i] += ' |'
                bridges[i] += '   |'
    bridges[n * 2 - 4] = bridges[2]
    bridges[n * 2 - 3] = '|/| |'
    while bridges[n * 2 - 3].__len__() != m * 2 - 3:
        bridges[n * 2 - 3] += ' |'
    bridges[n * 2 - 3] += '\|'
    bridges[n * 2 - 2] = bridges[0]


def main():
    if len(sys.argv) != 4:
        print("Неверные параметры!")
        return
    m = int(sys.argv[1])
    n = int(sys.argv[2])
    fname = sys.argv[3]
    if m <= 3 or n <= 3:
        print('Imaginary world!..')
        exit()
    if m % 2 != 0 and n % 2 != 0:
        print('Imaginary world!..')
        exit()
    if m % 2 != 0:
        if m == 5:
            m_five(n)
        else:
            m_uneven(m, n)
    elif n % 2 != 0:
        if n == 5:
            n_five(m)
        else:
            n_uneven(m, n)
    else:
        all_even(m, n)
    with open(fname, 'w') as output:
        for line in bridges:
            output.write(line + '\n')



main()
