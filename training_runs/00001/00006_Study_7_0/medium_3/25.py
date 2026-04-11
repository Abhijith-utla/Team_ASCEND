def sat(s: str):
    return str((8 ** 2888) ** 0.5).count(s) > 8 and len(s) == 3

def sol():
    import math
    answer = str((8 ** 2888) ** 0.5).count('0.31622776601683795') > 8 and len('0.31622776601683795') == 3
    return answer

print(sol())

if __name__ == "__main__":
    assert sat(sol())
