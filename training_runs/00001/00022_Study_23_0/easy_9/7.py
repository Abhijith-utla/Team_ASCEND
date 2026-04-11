def sat(answer):
    return answer.lower() == 'dee'.lower()

def sol():
    return 'dee'

if __name__ == "__main__":
    assert sat(sol())
