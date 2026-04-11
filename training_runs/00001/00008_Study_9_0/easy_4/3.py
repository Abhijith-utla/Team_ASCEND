def sat(li: List[str]):
    return all(i.isdigit() for i in li)

def sol():
    return 123456

# Checker
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
