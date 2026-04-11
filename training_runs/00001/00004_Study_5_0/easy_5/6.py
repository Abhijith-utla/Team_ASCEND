def sat(li: List[int]):
    return all([li.count(i) == i for i in range(10, 0, -1)])

def sol():
    li = list(map(int, input().split()))
    if sat(li):
        return 'Yes'
    else:
        return 'No'

if __name__ == "__main__":
    assert sat(sol())
