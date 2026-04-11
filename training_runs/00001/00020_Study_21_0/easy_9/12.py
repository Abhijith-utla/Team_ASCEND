def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(5)])

def sol():
    answer = []
    for i in range(5):
        answer.append(int(input()))
    return answer

def main():
    answer = sol()
    print(answer)
    assert sat(answer)

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    assert sat(sol())
