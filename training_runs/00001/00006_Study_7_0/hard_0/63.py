def sat(s: str):
    return str(8 ** 2888).count(s) > 8 and len(s) == 3

def sol():
    return 8 ** 2888 == int(8 ** 2888)

print(sol())  # print(True) if the function returns True else print(False)

if __name__ == "__main__":
    assert sat(sol())
