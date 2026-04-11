def sat(ls):
    return ls[1234] > ls[1235] and ls[1234] != ls[1235]

def sol():
    import random
    ls = [random.randint(1, 100) for _ in range(1000)]
    ls[1234] = ls[1235] = ls[1236] = ls[1237] = ls[1238] = ls[1239] = 100
    return ls

def sat(ls):
    return ls[1234] > ls[1235] and ls[1234] != ls[1235]

print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())
