def sat(ls, idx1=2, idx2=1):
    return ls[idx1] in ls[idx2] and ls[idx1] != ls[idx2]

def sol():
    return {'result': None}

def sat(ls):
    for idx1 in range(len(ls)):
        for idx2 in range(idx1 + 1, len(ls)):
            if ls[idx1] in ls[idx2] and ls[idx1] != ls[idx2]:
                return {'result': True}
    return {'result': False}

answer = sol()
assert sat(answer)

if __name__ == "__main__":
    assert sat(sol())
