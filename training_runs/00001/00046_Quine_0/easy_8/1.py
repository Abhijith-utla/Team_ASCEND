def sat(quine):
    return eval(quine + "()")

def sol():
    return 42

print(sat(sol))

if __name__ == "__main__":
    assert sat(sol())
