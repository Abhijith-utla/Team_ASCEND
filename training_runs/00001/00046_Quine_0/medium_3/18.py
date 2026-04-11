def sat(quine):
    return eval(quine + "()")

def sol():
    return "Hello, world!"

# Run the solution
print(sat(sol))

if __name__ == "__main__":
    assert sat(sol())
