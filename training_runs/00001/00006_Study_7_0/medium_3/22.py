def sat(s: str):
    return str((8 ** 2888) ** 0.5).count(s) > 8 and len(s) == 3

def sol():
    import math
    x = math.floor(math.log10(8**2888)) + 1
    y = math.floor(math.sqrt(10**(x-3)))
    z = math.floor(10**(x-3)) + 1
    return x, y, z

if __name__ == "__main__":
    assert sat(sol())
