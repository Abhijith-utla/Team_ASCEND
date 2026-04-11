def sat(x: float):
    return str(x - 3.1417).startswith("123.4567")

def sol():
    while True:
        x = float(input("Enter a number: "))
        if sat(x):
            return str(x)

def sat(x: float):
    return str(x - 3.1417).startswith("123.4567")

# test the solution
print(sol())

if __name__ == "__main__":
    assert sat(sol())
