def sat(li: List[int]):
    return all([li.count(i) == i for i in range(1, 11)])

def sol():
    return [i for i in range(1, 11) if [li.count(i) for li in range(1, 11)] != i]

# Checker
def checker(result):
    assert sat(result)

checker(sol())

if __name__ == "__main__":
    assert sat(sol())
