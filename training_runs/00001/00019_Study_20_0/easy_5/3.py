def sat(li: List[int]) -> bool:
    return all(li[i] <= li[i + 1] for i in range(len(li) - 1)) and li[0] <= li[-1]

def sol():
    return all(li[i] <= li[i + 1] for i in range(len(li) - 1)) and li[0] <= li[-1]

# test case
print(sat([1, 2, 3, 4, 5]))  # should return True
print(sat([5, 4, 3, 2, 1]))  # should return True
print(sat([1, 2, 3]))        # should return False
print(sat([5, 10, 15]))      # should return False

if __name__ == "__main__":
    assert sat(sol())
