def sat(li: List[int]):
    return li[li[0]] != li[li[1]] and li[li[1]] == li[li[2]]

def sol():
    return [2, 0, 1]

if __name__ == "__main__":
    assert sat(sol())
