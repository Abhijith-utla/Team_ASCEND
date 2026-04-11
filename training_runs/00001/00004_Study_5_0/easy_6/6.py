def sat(li: List[int]):
    return all([li.count(i) == i for i in range(10)])

def sol():
    answer = {
        'result': True,  # Replace 'True' with the correct answer
        'counts': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # Replace with the correct answer
    }
    return answer

if __name__ == "__main__":
    assert sat(sol())
