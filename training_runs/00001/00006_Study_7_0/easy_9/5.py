def sat(s: str):
    return (8 ** 2888) ** 0.5 > 8 and len(s) == 3

def sol():
    s = 'test'
    return (8 ** 2888) ** 0.5 > 8 and len(s) == 3

if __name__ == "__main__":
    assert sat(sol())
