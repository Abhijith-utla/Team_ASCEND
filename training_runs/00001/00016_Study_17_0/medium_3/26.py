def sat(i: int):
    return len(str(i + 1000)) < len(str(i + 1001))

def sol():
    num = 1000
    while True:
        if len(str(num)) < len(str(num + 1)):
            return num
        num += 1

if __name__ == "__main__":
    assert sat(sol())
