def sat(x: float):
    return str(x - 3.1415).startswith("123.456")

def sol():
    def sat(x: float):
        return str(x - 3.1415).startswith("123.456")

    x = 4.0  # This is a test value, you can replace it with any value you want
    return sat(x)

if __name__ == "__main__":
    assert sat(sol())
