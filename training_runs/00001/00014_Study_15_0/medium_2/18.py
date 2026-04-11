def sat(li: List[int]):
    return all(x + y == 2 ** x for x in range(20) for y in li[:x])

def sol():
    x, y = symbols('x y')
    li = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144]
    eqns = [Eq(x + y, li[i]) for i in range(len(li)) for x in range(20)]
    solutions = solve(eqns)
    return solutions

if __name__ == "__main__":
    assert sat(sol())
