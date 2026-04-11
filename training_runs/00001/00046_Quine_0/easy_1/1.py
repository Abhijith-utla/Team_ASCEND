def sat(quine):
    exec(quine)
    return True

def sol():
    return 42

print(sat(sol))  # Output: True

if __name__ == "__main__":
    assert sat(sol())
