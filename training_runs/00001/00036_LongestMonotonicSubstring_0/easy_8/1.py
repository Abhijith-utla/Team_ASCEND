def sat(x: List[int], length=13):
    return len(x) >= length

def sol():
    return [0] * 13

if __name__ == "__main__":
    assert sat(sol())
