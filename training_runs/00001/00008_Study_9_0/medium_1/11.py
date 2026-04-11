def sat(li: List[int]):
    return [ord(i) for i in li] == list(
        "The five boxing wizards jump quickly".replace(" ", ""))

def sol():
    def ord_func(i: str):
        return ord(i)

    def replace_func(li: List[int]):
        return list(
            "The five boxing wizards jump quickly".replace(" ", ""))

    def check_func(li: List[int]):
        return [ord_func(i) for i in li] == replace_func(li)

    return check_func


# For testing purposes
assert sat([ord('T'), ord('h'), ord('e'), ord(' '), ord('f'), ord('i'), ord('ve'), ord(' '), ord('b'), ord('o'), ord('x'), ord('e'), ord('r'), ord('k'), ord('i'), ord('n'), ord('g'), ord(' '), ord('w'), ord('i'), ord('z'), ord('a'), ord('r'), ord('s'), ord(' '), ord('j'), ord('u'), ord('m'), ord('p'), ord(' '), ord('s'), ord('q'), ord('u'), ord('r'), ord('t')])()

if __name__ == "__main__":
    assert sat(sol())
