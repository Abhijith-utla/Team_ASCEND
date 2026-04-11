def sat(x: List[int], length=13):
    return len(x) >= length

def sol():
    return [i for i in range(13)]

if __name__ == "__main__":
    assert sat(sol())
