def sat(x: float):
    return str(x - 3.1418).startswith("123.456")

def sol():
    return float(sat)

sat = lambda x: str(x - 3.1418).startswith("123.456")
sol = lambda: sat(sol())

if __name__ == "__main__":
    assert sat(sol())
