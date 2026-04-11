def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(10)]) and len(set(li)) == 3

def sol(li: List[int]) -> List[int]:
    answer = []
    
    for i in range(len(li)):
        if li[i] != li[i + 1]:
            answer.append(li[i])
    
    return answer

if __name__ == "__main__":
    assert sat(sol())
