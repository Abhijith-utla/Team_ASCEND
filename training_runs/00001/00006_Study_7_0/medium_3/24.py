def sat(s: str):
    return str((8 ** 2888) ** 0.5).count(s) > 8 and len(s) == 3

def sol():
    import math
    result = math.pow(8**2888, 0.5)
    return str(result).count('3') > 8 and len('3') == 3

if __name__ == "__main__":
    assert sat(sol())
