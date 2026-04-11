def sat(ls: List[str]):
    return "".join(ls) == str(1234567890)

def sol():
    return [str(i) for i in range(1, 10)]

print(sol())

if __name__ == "__main__":
    assert sat(sol())
