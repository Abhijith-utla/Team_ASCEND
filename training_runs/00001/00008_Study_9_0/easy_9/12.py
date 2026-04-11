def sat(li: List[int]):
    return [chr(i) for i in li] == list("Python is fun".replace(" ", ""))

def sol():
    return [chr(i) for i in [ord('P'), ord('y'), ord('t'), ord('h'), ord('o'), ord('n'), ord(' '), ord('i'), ord('s'), ord('f'), ord('u'), ord('n')]]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
