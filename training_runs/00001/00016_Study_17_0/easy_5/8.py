def sat(i: int) -> bool:
    return len(str(i + 10)) == len(str(i + 100))

def sol():
    for i in range(100):
        if sat(i):
            return i

if __name__ == "__main__":
    assert sat(sol())
