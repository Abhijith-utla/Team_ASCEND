def sat(s: str):
    return str(int(8 ** 2888)).count(s) > 8 and len(s) == 3

def solve(n: int, b: int, cnt: int, base: int):
        if n == 0:
            return cnt == 8 and base == 8
        d = n % b
        n //= b
        if d == 8:
            cnt += 1
        return solve(n, b, cnt, base * 10 + d)

    return solve(int(8 ** 2888), 8, 0, 0) and len(s) == 3

if __name__ == "__main__":
    assert sat(sol())
