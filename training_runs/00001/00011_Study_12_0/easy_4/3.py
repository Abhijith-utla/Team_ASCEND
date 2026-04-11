def sat(li: List[int]):
    return all(i + j == 3 for i, j in zip([4] + li, li)) and len(li) == 1000

def sol(li: List[int]):
    if len(li) != 1000:
        return False
    return sum(li) == 3

# Test the function
print(sol([4, 4, 4, 4, 4, 4, 4, 4, 4, 4]))  # Should print: True
print(sol([1, 2, 3

if __name__ == "__main__":
    assert sat(sol())
