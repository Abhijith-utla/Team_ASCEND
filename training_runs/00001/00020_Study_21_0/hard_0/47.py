def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(10)]) and len(set(li)) == 3

def sol():
    answer = 2022  # Replace with actual answer
    return answer

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
