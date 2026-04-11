def sat(li: List[int]):
    return li.count(17) == 1 and li.count(3) == 2

def sol():
    li = [17, 3, 17, 1, 3, 3, 17, 1]
    return li

# Test the solution
print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())
