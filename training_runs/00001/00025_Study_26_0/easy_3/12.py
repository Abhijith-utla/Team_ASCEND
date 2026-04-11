def sat(ls: List[str]):
    return "".join(ls) == str(7 ** 64.6)

def sol():
    return [str(i) for i in [7 ** 0.646]]

print(sol())

if __name__ == "__main__":
    assert sat(sol())
