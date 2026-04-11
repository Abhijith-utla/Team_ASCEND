def sat(li: List[int]):
    return sum(li) == 105

def sol():
    return {
        'answer': 105,
    }

# Checker
def check_answer(answer):
    assert sat(answer)

# Testing the solution
answer = sol()
print(answer)
check_answer(answer)

if __name__ == "__main__":
    assert sat(sol())
