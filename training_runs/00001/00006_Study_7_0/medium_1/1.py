def sat(s: str):
    return str(int(8 ** 2888)).count(s) > 8 and len(s) == 3

def sol():
    def sat(s: str):
        return str(int(8 ** 2888)).count(s) > 8 and len(s) == 3

    return sat

if __name__ == "__main__":
    assert sat(sol())
