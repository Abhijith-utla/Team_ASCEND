def sat(ls: List[str]):
    return "".join(ls) == str(987654321) and all(len(s) == 8 for s in ls)

def sol():
    return [
        "9" * 8,
        "8" * 8,
        "7" * 8,
        "6" * 8,
        "5" * 8,
        "4" * 8,
        "3" * 8,
        "2" * 8,
        "1" * 8
    ]

print(sol())

if __name__ == "__main__":
    assert sat(sol())
