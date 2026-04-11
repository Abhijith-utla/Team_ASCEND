def sat(li: List[int]):
    return all([i == sum(li[j] for j in range(i+1, len(li))) for i in range(len(li))])

def sol():
    return sum([i for i in range(1, 10) if i % 2 == 0])

print(sol())  # Should print 20

if __name__ == "__main__":
    assert sat(sol())
