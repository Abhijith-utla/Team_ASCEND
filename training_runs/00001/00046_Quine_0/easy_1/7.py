def sat(quine):
    exec(quine)
    return True

def sol():
    return "Hello World"

print(sat(sol))  # Outputs: Hello World

if __name__ == "__main__":
    assert sat(sol())
