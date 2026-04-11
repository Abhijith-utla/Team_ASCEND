def sat(li: List[int]):
    return all(x >= 0 and x in range(20) for x in li)

def sol():
    answer = sum([i for i in range(20) if i not in range(0, 20, 3)])
    return answer

print(sol())

if __name__ == "__main__":
    assert sat(sol())
