import math


def hola_mundo():
    print('Hola Mundo')


def calculate_sqrt(num):
    return math.sqrt(num)


def main_func(length):
    hola_mundo()
    print([x * 2 for x in range(length)])
    while True:
        num = float(input('type a number: '))
        res = calculate_sqrt(num)
        print(f'The Square of the number {num} is {res}')


if __name__ == '__main__':
    main_func(10)
