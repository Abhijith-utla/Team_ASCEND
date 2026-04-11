def sat(x: float):
    return str(x - 3.1415).startswith("123.456")

def sol():
    answer = None
    x = 0.0
    while not sat(x):
        x += 1.0
    answer = x
    return answer

if __name__ == "__main__":
    assert sat(sol())
