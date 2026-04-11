def sat(li: List[int]):
    return all([li.count(i) == i for i in range(1, 11)])

def sol():
    li = [int(i) for i in input().split()]
    if sat(li):
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":
    assert sat(sol())
