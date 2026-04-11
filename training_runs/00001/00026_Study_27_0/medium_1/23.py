def sat(li: List[int]):
    return li[li[0]] != li[li[1]] and li[li[2]] == li[li[3]]

def sol():
    return [2, 3, 0, 1]

print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())
