def sat(li: List[int]):
    return li[li[0]] != li[li[1]] and li[li[li[0]]] == li[li[li[1]]]

def sol():
    def inner(a: int, b: int):
        return a != b and a == b
    
    a = [inner(1, 2)]
    a[0] = a[1] = 3
    return a

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
