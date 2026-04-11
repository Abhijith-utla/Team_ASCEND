def sat(li: List[str]):
    return sum([1 for i in li if ord(i) % 3 == 2]) == 0

def sol():
    return [chr(i) for i in range(97, 123) if (ord(chr(i)) % 3 == 2)]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
