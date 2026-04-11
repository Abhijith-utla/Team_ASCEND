def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(10)]) and len(set(li)) == 3

def sol():
    li = [random.randint(1, 10) for _ in range(11)]  # randomly generated list
    assert sat(li)
    return li

if __name__ == "__main__":
    assert sat(sol())
