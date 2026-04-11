def sat(s: str):
    return str(8 ** 2888).count(s) > 8 and len(s) == 3

def sol():
    def check(s: str):
        return str(8 ** 2888).count(s) > 8 and len(s) == 3

    left, right = 0, 10000
    while left < right:
        mid = (left + right) // 2
        if check(str(mid)):
            right = mid
        else:
            left = mid + 1

    return str(right)

print(sol())

if __name__ == "__main__":
    assert sat(sol())
