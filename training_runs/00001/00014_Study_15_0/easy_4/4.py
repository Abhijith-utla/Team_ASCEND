def sat(li: List[int]):
    return all(x + y == 2 ** x for x in range(20) for y in li[:x])

def sol():
    li = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864]
    return all(x + y == 2 ** x for x in range(20) for y in li[:x])

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
