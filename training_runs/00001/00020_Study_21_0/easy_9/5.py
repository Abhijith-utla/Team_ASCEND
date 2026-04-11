def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(5)])

def sol():
    answer = []
    for i in range(5):
        answer.append(i+1)
    return answer

# Checking the answer
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
