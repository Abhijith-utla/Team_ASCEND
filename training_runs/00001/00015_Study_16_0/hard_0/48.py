def sat(s: str):
    return float(s) + len(s) == 4.5

def sol():
    return len("1234") + float("1234") == 4.5

print(sol())

if __name__ == "__main__":
    assert sat(sol())
