def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(9)]) and len(set(li)) == 3

def sol():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]

# The function 'sat' is already defined by the user.
# Therefore, no modification is needed.

if __name__ == "__main__":
    assert sat(sol())
