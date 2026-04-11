def sat(s: str) -> bool:
    return str(8 ** int(2888)).count(s) > 8 and len(s) == 5

def sol():
    for i in range(2888):
        if str(8 ** i).count('88888') > 8:
            return True
    return False

if __name__ == "__main__":
    assert sat(sol())
