def sat(x: float):
    return str(x - 3.1415).startswith("123.456")

def sol():
    answer = 123.456
    return answer

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
