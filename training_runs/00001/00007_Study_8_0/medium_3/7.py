def sat(ls, idx1=1234, idx2=1235, value=ls[idx1]):
    return ls[idx1] in ls[idx2] and ls[idx1] != value

def sol():
    return {
        'answer': {
            'idx1': 1234,
            'idx2': 1235,
            'value': 123456,
            'result': sat(ls, idx1=1234, idx2=1235, value=ls[idx1])
        }
    }

def sat(ls, idx1=1234, idx2=1235, value=ls[idx1]):
    return ls[idx1] in ls[idx2] and ls[idx1] != value

if __name__ == "__main__":
    ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    answer = sol()
    print(answer['answer'])
    assert sat(ls, idx1=answer['answer']['idx1'], idx2=answer['answer']['idx2'], value=answer['answer']['value'])

if __name__ == "__main__":
    assert sat(sol())
