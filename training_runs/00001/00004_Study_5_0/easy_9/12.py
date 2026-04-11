def sat(li: list) -> bool:
    return all([li.count(i) == i for i in range(10)]) == li.count(0) == 1

def sol():
    def sat(li: list) -> bool:
        return all([li.count(i) == i for i in range(10)]) == li.count(0) == 1

    li = [0]*10 + [1]*5
    assert sat(li)
    return li

print(sol())

if __name__ == "__main__":
    assert sat(sol())
