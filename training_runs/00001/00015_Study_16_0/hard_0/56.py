def sat(s: str):
    return float(s) + len(s) == 4.5

def sol():
    return float(str(len("test"))) + len("test") == 4.5

print(sol())

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
