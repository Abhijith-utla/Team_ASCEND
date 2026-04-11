def sat(li: List[int]):
    return li[li[0]] != li[li[1]] and li[li[2]] == li[li[3]]

def sol():
    answer = [4, 2, 3, 5]
    return answer

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
