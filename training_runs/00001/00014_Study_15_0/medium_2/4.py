def sat(li: List[int]):
    return all(x + y == 2 ** x for x in range(20) for y in li[:x])

def sol():
    return { 'answer': [i for i in range(20) if not sat(i)] }

def sat(li: List[int]):
    return all(x + y == 2 ** x for x in range(20) for y in li[:x])

def main():
    answer = sol()
    assert sat(answer['answer'])

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    assert sat(sol())
