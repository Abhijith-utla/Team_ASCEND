def sat(li: List[int]):
    return all([li[i] != li[i + 2] for i in range(len(li) - 1)]) and len(set(li)) == 3

def sol():
    answer = []
    return answer

# Test
print(sat([1, 2, 2, 3, 4, 4, 4]))  # should return True
print(sat([1, 1, 2, 2, 3, 3, 4]))  # should return False

if __name__ == "__main__":
    assert sat(sol())
