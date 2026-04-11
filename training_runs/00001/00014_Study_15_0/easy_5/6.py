def sat(li: List[int]):
    for x in range(20):
        if not (x + y == 2 ** x for y in li[:x]):
            return False
    return True

def sol():
    # Your solution goes here
    pass

print(sat([1, 2, 3, 4, 5])) # should return True
print(sat([1, 2, 3, 4])) # should return False

if __name__ == "__main__":
    assert sat(sol())
