def sat(li: List[int]):
    return all(i + j == 9 for i, j in zip([4] + li, li)) and len(li) == 1000

def sol(li: List[int]) -> List[int]:
    answer = [0]*1000
    for i in range(1000):
        if i < len(li):
            answer[i] = li[i]
    return answer

if __name__ == "__main__":
    assert sat(sol())
