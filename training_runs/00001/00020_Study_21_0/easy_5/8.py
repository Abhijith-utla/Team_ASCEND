def sat(li: List[int]):
    return all(li[i] != li[i + 1] for i in range(8) and len(set(li)) == 3)

def sol():
    answer = []
    for i in range(10):
        answer.append(i)
    return answer

# This assertion test checks if the solution function works correctly
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
