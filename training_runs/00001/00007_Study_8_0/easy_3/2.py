def sat(ls):
    return ls[1234] < ls[1235] and ls[1234] != ls[1235]

def sol():
    import random
    ls = [random.randint(0,100) for _ in range(1000)]
    assert sat(ls)
    return ls[1234] < ls[1235] and ls[1234] != ls[1235]

def sat(ls):
    return ls[1234] < ls[1235] and ls[1234] != ls[1235]

print(sol())

if __name__ == "__main__":
    assert sat(sol())
