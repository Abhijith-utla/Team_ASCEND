def sat(ls: List[str]):
    return min(ls) == max(ls) == str(len(ls))

def sol():
    return [str(len(ls)) for ls in [[i for i in range(10)] * 10] * 10]

if __name__ == "__main__":
    assert sat(sol())
