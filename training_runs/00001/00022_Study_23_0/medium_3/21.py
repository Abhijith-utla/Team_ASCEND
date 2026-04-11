def sat(answer):
    return all(answer[i] == 'dee'[i] for i in range(len(answer)))

def sol():
    return "dee"

if __name__ == "__main__":
    assert sat(sol())
