def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(8)]) and len(set(li)) == 3

def sol():
    def sat(li: List[int]):
        return all([li[i] != li[i + 1] for i in range(8)]) and len(set(li)) == 3
    
    answer = []
    
    for i in range(10):
        answer.append(i)
        
    answer.append(10)
    answer.append(15)
    answer.append(15)
    answer.append(20)
    
    assert sat(answer)
    return answer

if __name__ == "__main__":
    assert sat(sol())
