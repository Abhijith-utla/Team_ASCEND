def sat(s: str):
    return (8 ** 2888) ** 0.5 > 8 and len(s) == 3

def sol():
    s = '888'
    return (8 ** 2888) ** 0.5 > 8 and len(s) == 3

print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())
