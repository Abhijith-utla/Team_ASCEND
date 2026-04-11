def sat(ls, idx1=1234, idx2=1235):
    return ls[idx1] in ls[idx2] and ls[idx1] != ls[idx2]

def sol():
    return {
        'answer1': sat([1, 2, 3, 4, 5, 6, 7, 8, 9]),
        'answer2': sat(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']),
        'answer3': sat(['apple', 'banana', 'cherry', 'date', 'elderberry']),
        'answer4': sat([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    }

print(sol())

if __name__ == "__main__":
    assert sat(sol())
