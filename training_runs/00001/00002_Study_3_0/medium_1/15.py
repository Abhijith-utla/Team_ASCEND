def sat(li: List[int]):
    return sorted(li) == list(range(999)) and all(li[i] != i for i in range(len(li)))

def sol():
    return <answer>

if __name__ == "__main__":
    assert sat(sol())
