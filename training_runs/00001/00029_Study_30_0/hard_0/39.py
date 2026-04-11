def sat(li: List[int]):
    return all([123 * li[i] % 1000 < 123 * li[i + 1] % 1000 and li[i] in range(1000) for i in range(20)])

def sol():
    def mod_1000(n: int) -> int:
        return n % 1000 if n >= 0 else -(-n % 1000)

    def check(li: List[int]) -> bool:
        return all([mod_1000(123 * li[i] % 1000) < 123 * mod_1000(li[i + 1] % 1000) and li[i] in range(1000) for i in range(20)])

    return check([randint(0, 999) for _ in range(20)])

if __name__ == "__main__":
    assert sat(sol())
