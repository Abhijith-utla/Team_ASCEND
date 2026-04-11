def sat(s: str):
    return str(int(8 ** 2888)).count(s) == 10 and len(s) == 3

def sol():
    return "8"*2888 if sat(str(int(8 ** 2888))) else "Unsatisfiable"

print(sol())

if __name__ == "__main__":
    assert sat(sol())
