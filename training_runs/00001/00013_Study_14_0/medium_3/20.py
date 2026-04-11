def sat(li: List[int]):
    return all([i == sum(li[j] for j in range(i+1, len(li))) for i in range(len(li))])

def sol():
    return {
        "li": [1, 2, 3, 4, 5],
        "answer": sat(sol().get("li"))
    }

def sat(li: List[int]):
    return all([i == sum(li[j] for j in range(i+1, len(li))) for i in range(len(li))])

print(sat(sol().get("li")))  # True
print(sat(sol().get("li")))  # False

if __name__ == "__main__":
    assert sat(sol())
