def sat(li: List[int]):
    return all([i == sum(li[j] for j in range(i+1, len(li))) for i in range(len(li))])

def sol():
    return [sum(li[j] for j in range(i+1, len(li))) for i in range(len(li))]

print(sol())

if __name__ == "__main__":
    assert sat(sol())
