def sat(li: List[int]):
    return all(li[i] != li[i + 1] for i in range(8) if len(set(li)) == 3)

def sol():
    return [2, 3, 5, 7, 11, 13, 17, 19]

if __name__ == "__main__":
    assert sat(sol())
