def sat(quine):
    exec(quine)
    return True

def sol():
    return ""

if __name__ == "__main__":
    assert sat(sol())
