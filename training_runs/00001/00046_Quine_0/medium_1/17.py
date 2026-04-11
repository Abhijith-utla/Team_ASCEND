def sat(quine):
    return eval(quine) == quine

def sol():
    return {}

print(sat(sol)) # False

if __name__ == "__main__":
    assert sat(sol())
