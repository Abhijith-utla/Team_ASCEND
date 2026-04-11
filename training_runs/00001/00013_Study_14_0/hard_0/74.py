def sat(li: List[int]):
    return all([sum(li[:i]) == i for i in range(20)])

def sol():
    def sat(li: List[int]):
        return all([sum(li[:i]) == i for i in range(20)])

    answer = sat([1]*20)
    return answer

answer = sol()
print(answer)

if __name__ == "__main__":
    assert sat(sol())
