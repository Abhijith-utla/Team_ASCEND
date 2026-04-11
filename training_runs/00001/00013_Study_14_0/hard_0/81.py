def sat(li: List[int]):
    return all([sum(li[:i]) == i for i in range(20)])

def sol():
    def sat(li: List[int]):
        return all([sum(li[:i]) == i for i in range(20)])

    return sat([1]*20)

# Test case
print(sol()) # False

if __name__ == "__main__":
    assert sat(sol())
