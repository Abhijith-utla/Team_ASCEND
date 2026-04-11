def sat(li: List[int]):
    return all([i == sum(li[j] for j in range(i+1, len(li))) for i in range(len(li))])

def sol(li: List[int]) -> int:
    answer = sum(li)
    for i in range(len(li)):
        if li[i] != sum(li[j] for j in range(i+1, len(li))):
            answer = 0
            break
    return answer

if __name__ == "__main__":
    assert sat(sol())
