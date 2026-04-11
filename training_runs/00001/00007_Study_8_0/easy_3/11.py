def sat(ls):
    return ls[1234] < ls[1235] and ls[1234] != ls[1235]

def sol():
    result = [12345]*1000000
    return result

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
