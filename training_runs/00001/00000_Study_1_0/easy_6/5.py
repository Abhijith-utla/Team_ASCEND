def sat(s: str):
    return s.count('oo') <= 1

def sol():
    def sat(s: str):
        return s.count('oo') <= 1

    return sat('oo')

if __name__ == "__main__":
    assert sat(sol())
