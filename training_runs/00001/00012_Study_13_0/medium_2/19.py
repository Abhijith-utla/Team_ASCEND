def sat(x: float):
    return str(x - 3.1416).startswith("123.456")

def sol():
    return float(input("Enter a number: ")) - 3.1416

print(sol())

# Checker
def check_sol(x):
    assert sat(x)

check_sol(sol())

if __name__ == "__main__":
    assert sat(sol())
