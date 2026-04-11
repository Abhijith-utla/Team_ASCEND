def sat(li: List[str]):
    return sum([1 for i in li if ord(i) % 3 == 2]) == 0

def sol():
    return sum([1 for i in range(10) if ord(chr(i+65)) % 3 == 2]) == 0

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
