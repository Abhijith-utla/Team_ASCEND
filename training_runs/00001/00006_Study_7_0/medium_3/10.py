def sat(s: str):
    return str((8 ** 2888) ** 0.5).count(s) > 8 and len(s) == 3

def sol():
    return (8 ** 2888) ** 0.5 == round((8 ** 2888) ** 0.5)

print(sol())

if __name__ == "__main__":
    assert sat(sol())
