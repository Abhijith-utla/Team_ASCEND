def sat(li: List[int]) -> bool:
    return all([j == 3 * i for j, i in enumerate(li)])

def sol():
    li = [i for i in range(1, 11) if i % 3 == 0]
    return li

print(sol())

if __name__ == "__main__":
    assert sat(sol())
