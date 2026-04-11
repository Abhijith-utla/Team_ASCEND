def sat(li):
    return li[li[0]] == li[li[1]]

def sol():
    answer = [1, [1, 2]]
    return answer

if __name__ == "__main__":
    assert sat(sol())
