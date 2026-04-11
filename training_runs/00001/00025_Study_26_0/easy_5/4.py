def sat(ls: List[str]):
    return "".join(ls) == str(123456789)

def sol():
    return [str(num) for num in range(1, 10)]

if __name__ == "__main__":
    assert sat(sol())
