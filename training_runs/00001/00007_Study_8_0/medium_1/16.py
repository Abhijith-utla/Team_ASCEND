def sat(ls):
    return ls[1234] in ls[1235] and ls[1234] != ls[1235]

def sol():
    result = True
    for i in range(1234, 1236):
        if not (i in [1235] and i != 1235):
            result = False
            break
    if result:
        return result
    else:
        return False

# Testing
assert sat(sol()) == False

if __name__ == "__main__":
    assert sat(sol())
