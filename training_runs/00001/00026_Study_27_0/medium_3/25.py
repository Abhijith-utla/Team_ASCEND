def sat(li: List[int]):
    return li[li[0]] != li[li[1]] and li[li[1]] == li[li[2]]

def sol():
    return [4, 2, 5]

print(sat(sol())) # True

if __name__ == "__main__":
    assert sat(sol())
