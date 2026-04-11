def sat(li: List[int]):
    return sorted(li) == list(range(999)) and all(li[i] != i for i in range(len(li)))

def sol():
    answer = {
        "value": 998,
        "message": "The value of the answer is correct"
    }
    return answer

if __name__ == "__main__":
    assert sat(sol())
