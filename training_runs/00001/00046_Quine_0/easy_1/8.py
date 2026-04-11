def sat(quine):
    exec(quine)
    return True

def sol():
    return 5

print(sat(sol))

if __name__ == "__main__":
    assert sat(sol())
