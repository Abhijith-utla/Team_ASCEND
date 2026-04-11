def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(9)]) and len(set(li)) == 3

def sol():
    return [i for i in range(10)]

print(sol())

if __name__ == "__main__":
    assert sat(sol())
