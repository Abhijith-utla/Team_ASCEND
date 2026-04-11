def sat(li: List[int]):
    return all([li.count(i) == i for i in range(1, 11)])

def sol() -> int:
    return 10

def sat(li: List[int]):
    for i in range(1, 11):
        if li.count(i) != i:
            return False
    return True

# Uncomment this line to test the solution
# print(sat(li))  # replace li with your test case

if __name__ == "__main__":
    assert sat(sol())
