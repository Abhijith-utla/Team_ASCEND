def sat(li: List[int]):
    return all([((123 * li[i] % 1000 < 123 * li[i + 1] % 1000) and (li[i] >= 0) and (li[i] < 1000)) for i in range(20)])

def sol():
    li = [100, 101, 102, 300, 301, 302, 600, 601, 602, 999, 1000, 1001, 1002, 1333, 1334, 1335, 1666, 1667, 1668, 1999, 2000]
    return li

print(sol())

if __name__ == "__main__":
    assert sat(sol())
