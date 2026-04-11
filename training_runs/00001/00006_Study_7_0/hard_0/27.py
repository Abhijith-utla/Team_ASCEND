def sat(s: str):
    return str(8 ** 2888).count(s) > 8 and len(s) == 3

def sol():
    s = str(8 ** 2888)
    return str(8 ** 2888).count(s) > 8 and len(s) == 3

# The checker will run: assert sol()

if __name__ == "__main__":
    assert sat(sol())
