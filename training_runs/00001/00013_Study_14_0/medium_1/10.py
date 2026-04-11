def sat(li: List[int]):
    return all([i < sum(li[:i]) for i in range(20)])

def sol():
    def sat(li: List[int]):
        return all([i < sum(li[:i]) for i in range(20)])

    answer = sat([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    return answer

print(sol())

if __name__ == "__main__":
    assert sat(sol())
