def sat(li: List[int]) -> bool:
    if len(li) != 10:
        return False
    if li.count(li[3]) != 2:
        return False
    return True

def sol():
    answer = []
    for i in range(10):
        if i != 3:
            answer.append(i)
        else:
            answer.append(2)
    return answer

if __name__ == "__main__":
    assert sat(sol())
