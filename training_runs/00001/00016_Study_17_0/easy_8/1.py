def sat(i: int) -> bool:
    return len(str(i)) < len(str(i + 1))

def sol():
    i = 10
    while True:
        if sat(i):
            return i
        i += 1

if __name__ == "__main__":
    assert sat(sol())
