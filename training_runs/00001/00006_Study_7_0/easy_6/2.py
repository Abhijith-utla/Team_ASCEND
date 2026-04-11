def sat(s: str) -> bool:
    return str(8 ** int(2888)).count(s) > 8 and len(s) == 5

def sol():
    return sat('10201')

if __name__ == "__main__":
    assert sat(sol())
