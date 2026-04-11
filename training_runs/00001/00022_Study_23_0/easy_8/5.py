def sat(answer):
    return answer.startswith('dee')

def sol():
    answer = 'deep learning'
    return answer

if __name__ == "__main__":
    assert sat(sol())
