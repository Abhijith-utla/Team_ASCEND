def sat(ls):
    return ls[1234] in ls[1235] and ls[1234] != ls[1235]

def sol():
    result = {}
    for i in range(1234, 1235):
        result[i] = [i]
    return result

# Testing
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
