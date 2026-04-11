def sat(ls: List[str]):
    return "".join(ls) == str(12345678)

def sol():
    return ""

# Final checker will run: assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
