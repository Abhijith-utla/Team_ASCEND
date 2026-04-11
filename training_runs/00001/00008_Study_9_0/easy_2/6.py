def sat(li: List[str]):
    return sum([1 for i in li if ord(i) % 3 == 1]) == 0

def sol():
    return [chr(i) for i in range(32, 256) if ord(chr(i)) % 3 == 1]

if __name__ == "__main__":
    assert sat(sol())
