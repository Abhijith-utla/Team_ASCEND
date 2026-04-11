def sat(li: List[int]):
    return all([sum(li[:i]) == i for i in range(20)])

def sol():
    def sat(li: List[int]):
        return all([sum(li[:i]) == i for i in range(20)])
    
    answer = []
    for i in range(20):
        temp = [j for j in range(i+1)]
        if sat(temp):
            answer.append(i)
    
    return answer

if __name__ == "__main__":
    assert sat(sol())
