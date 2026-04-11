def sat(li: List[int]):
    # Check if all elements in the list are either 0, 1, or 3 times their position
    return all(j in {i - 1, i + 1, 3 * i} for i, j in enumerate(li, start=1))

def sol():
    answer = []
    for i in range(1, 101):
        if i == 1 or i == 100:
            answer.append(i)
        elif i == 2 or i == 98:
            answer.append(i)
        elif i == 3 or i == 99:
            answer.append(i)
        else:
            answer.append(3 * i)
    return answer

print(sol())

if __name__ == "__main__":
    assert sat(sol())
