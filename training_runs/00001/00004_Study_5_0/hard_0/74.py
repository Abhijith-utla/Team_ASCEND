def sat(li: List[int]):
    return all([li.count(i) == i for i in range(10)])

def sol():
    return 11

# You can verify the answer by running the following code:
# assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
