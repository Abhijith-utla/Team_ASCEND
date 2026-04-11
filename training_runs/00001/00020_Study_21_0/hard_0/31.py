def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(10)]) and len(set(li)) == 3

def sol():
    def is_sorted(li: List[int]):
        return li == sorted(li)

    def has_unique_elements(li: List[int]):
        return len(li) == len(set(li))

    def all_unique(li: List[int]):
        return all([has_unique_elements(li), is_sorted(li)])

    return all_unique([randint(1, 100) for _ in range(10)])

# Run the solution
print(sol())

if __name__ == "__main__":
    assert sat(sol())
