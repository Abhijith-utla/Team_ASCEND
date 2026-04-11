def sat(quine):
    return eval(quine + "()")

def sol():
    return None

print(sat(sol))

if __name__ == "__main__":
    assert sat(sol())
