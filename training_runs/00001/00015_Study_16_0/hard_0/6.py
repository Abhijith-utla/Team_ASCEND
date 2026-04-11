def sat(s: str):
    return float(s) + len(s) == 4.5

def sol():
    return float(input("Please enter a number: ")) + len(input("Please enter a string: ")) == 4.5

if __name__ == "__main__":
    assert sat(sol())
