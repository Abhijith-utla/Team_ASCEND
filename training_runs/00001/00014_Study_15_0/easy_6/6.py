def sat(li: List[int]):
    return all(x + y == 2 ** x for x in range(20) for y in li[:x + 1])

def sol():
    li = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]
    return all(x + y == 2 ** x for x in range(20) for y in li[:x + 1])

if __name__ == "__main__":
    assert sat(sol())
