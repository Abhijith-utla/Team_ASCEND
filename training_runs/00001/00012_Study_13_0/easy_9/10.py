def sat(x: float):
    return str(x - 3.1418).startswith("123.456")

def sol():
    answer = 3.1418
    return str(answer)

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
