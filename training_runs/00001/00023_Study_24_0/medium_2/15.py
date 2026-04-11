def sat(li: List[int]):
    return li.count(17) == 2 and li.count(3) == 1

def sol():
    answer = []
    for i in range(10):
        answer.append(17)
        if len(answer) == 2:
            break
        answer.append(3)
    return answer

# Test the function
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
