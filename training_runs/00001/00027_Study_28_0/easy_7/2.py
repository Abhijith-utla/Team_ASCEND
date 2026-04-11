def sat(li):
    for i in li:
        for j in li:
            if abs(i - j) < 10:
                return False
    return len(li) == 100

def sol():
    li = [i for i in range(100)]
    return li

# Testing
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
