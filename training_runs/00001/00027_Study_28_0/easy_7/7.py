def sat(li):
    for i in li:
        for j in li:
            if abs(i - j) < 10:
                return False
    return len(li) == 100

def sol():
    return [i for i in range(100) if not sat([i]*100)]

# checker
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
