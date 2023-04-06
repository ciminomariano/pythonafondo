import ctypes


def literal():
    pointer = id(42)
    pointer2 = id(42)
    pointer3 = id(43)
    return pointer, pointer2, pointer3


if __name__ == '__main__':
    pointers = literal()

    print(pointers)
